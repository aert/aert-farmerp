django:
  path: /www/aert_bookkeeping/site
  requirements: /www/aert_bookkeeping/site/requirements/staging.txt
  settings: aert_bookkeeping.settings.staging
  virtualenv: /www/aert_bookkeeping/env
  user: www-data
  group: www-data
  git_repo: https://github.com/aert/aert-bookkeeping.git
  git_rev: master
