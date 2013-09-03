include:
  - uwsgi

bookkeeping-uwsgi:
  file.managed:
    - name: /etc/uwsgi/apps-available/bookkeeping.ini
    - source: salt://aert_bookkeeping/uwsgi.ini
    - template: jinja
    - user: www-data
    - group: www-data
    - mode: 755
    - require:
      - pip: uwsgi

enable-uwsgi-app:
  file.symlink:
    - name: /etc/uwsgi/apps-enabled/bookkeeping.ini
    - target: /etc/uwsgi/apps-available/bookkeeping.ini
    - force: false
    - require:
      - file: bookkeeping-uwsgi
      - file: /etc/uwsgi/apps-enabled
