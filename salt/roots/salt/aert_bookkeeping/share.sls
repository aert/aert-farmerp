
{{ pillar['django']['path'] }}:
  file.directory:
    - user: {{ pillar['django']['user'] }}
    - group: {{ pillar['django']['group'] }}
    - makedirs: True