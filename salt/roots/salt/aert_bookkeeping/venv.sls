include:
  - aert_bookkeeping.requirements
  - aert_bookkeeping.share

virtualenvwrapper:
  pip.installed

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
      - pip: virtualenvwrapper

bookkeeping_env_postactivate:
  file.managed:
    - name: {{ pillar['django']['virtualenv'] }}/bin/postactivate
    - source: salt://aert_bookkeeping/venv.postactivate
    - template: jinja
    - user: www-data
    - group: www-data
    - mode: 755
    - require:
      - virtualenv: {{ pillar['django']['virtualenv'] }}

