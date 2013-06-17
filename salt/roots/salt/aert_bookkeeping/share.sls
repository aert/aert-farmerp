include:
  - aert_bookkeeping.requirements
  

{{ pillar['django']['path'] }}:
  file.directory:
    - user: {{ pillar['django']['user'] }}
    - group: {{ pillar['django']['group'] }}
    - makedirs: True

webapp:
  git.latest:
    - name: {{ pillar['django']['git_repo'] }}
    - rev: {{ pillar['django']['git_rev'] }}
    - target: {{ pillar['django']['path'] }}
    - force: true
    - require:
      - pkg: bookkeeping-packages
