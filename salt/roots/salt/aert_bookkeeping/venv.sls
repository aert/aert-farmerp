include:
  - aert_bookkeeping.requirements
  - aert_bookkeeping.share

# Create the Python Virtual environment
{{ pillar['django']['virtualenv'] }}:
  virtualenv.managed:
    - no_site_packages: True
    - distribute: True
    - runas: {{ pillar['django']['user'] }}
    - require:
      - pkg: bookkeeping-packages
      - file: {{ pillar['django']['path'] }}
      - git: webapp

