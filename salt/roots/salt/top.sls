base:
  '*':
    - requirements.essential
    - ssh
  'vagrant.aert-bookkeeping.org':
    - aert_bookkeeping.requirements
    - aert_bookkeeping.nginx
    - aert_bookkeeping.share
    - aert_bookkeeping.venv
    - aert_bookkeeping.pip
    - aert_bookkeeping.wheel
#    - aert_bookkeeping.uwsgi
    - aert_bookkeeping.postgresql

