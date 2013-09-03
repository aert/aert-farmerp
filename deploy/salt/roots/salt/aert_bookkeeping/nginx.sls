include:
  - nginx

bookkeeping-nginx-conf:
  file.managed:
    - name: /etc/nginx/sites-available/aert-bookkeeping.conf
    - source: salt://aert_bookkeeping/nginx.conf
    - template: jinja
    - user: www-data
    - group: www-data
    - mode: 755
    - require:
      - pkg: nginx

# Symlink and thus enable the virtual host
bookkeeping-enable-nginx:
  file.symlink:
    - name: /etc/nginx/sites-enabled/aert-bookkeeping.conf
    - target: /etc/nginx/sites-available/aert-bookkeeping.conf
    - force: false
    - require:
      - file: bookkeeping-nginx-conf