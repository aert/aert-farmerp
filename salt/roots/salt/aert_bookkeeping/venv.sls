
# Create the Python Virtual environment
{{ pillar['django']['virtualenv'] }}:
  virtualenv.managed:
    - no_site_packages: True
    - distribute: True
    - runas: {{ pillar['django']['user'] }}
    - require:
      - pkg: python-virtualenv
      - pkg: python-dev
      - pkg: libpq-dev