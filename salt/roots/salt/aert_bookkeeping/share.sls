
{{ pillar['django']['path'] }}::
  file.directory:
    - user: www-data
    - makedirs: True