
Installation
************
 
Local
=====

Development environment::

  $ fab init_env_local
  $ fab init_env_vagrant

Staging
=======

Using vagrant by default:

#. Add hosts in ``deploy/ansible/hosts/staging``.
#. Set environment vars in ``deploy/ansible/vars/staging.yml``.
#. Launch installation wizard::

   $ fab deploy_staging

Production
==========

#. Add hosts in ``deploy/ansible/hosts/production``
#. Set environment vars in ``deploy/ansible/vars/production.yml``
#. Launch installation wizard::

   $ fab deploy_prod
