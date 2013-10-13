Farm ERP
''''''''

.. image:: https://travis-ci.org/aert/farmerp.png?branch=master
        :target: https://travis-ci.org/aert/farmerp

**Warning:** This project is currently in an **alpha** state and currently not meant for real projects.

Introduction
************
 
Accounting software relying on `FAO guidelines`_.

Notable features:

* Cash Journal
* Credit Book
* Product Inventory
* User Management

Requirements 
************
 
Dependencies
============
 
* Debian 7 (or Ubuntu >= 12.04)
* Python 2.7
* Vagrant *(Optional, to test staging env)*
* Ansible *(Optional, to test staging env)*
* sshpass *(Optional, to setup Vagrant VM)*


Installation
************
 
* Local (development)::

     $ fab init_env_local
     $ fab init_env_vagrant

* Staging:

  #. Add hosts in ``deploy/ansible/hosts/staging``.
  #. Set environment vars in ``deploy/ansible/vars/staging.yml``.
  #. Launch installation wizard::

       $ fab deploy_staging

* Production:

  #. Add hosts in ``deploy/ansible/hosts/production``
  #. Set environment vars in ``deploy/ansible/vars/production.yml``
  #. Launch installation wizard::

     $ fab deploy_prod


Usage
*****

* Local::

    $ fab run_server
    $ xdg-open http://192.168.111.222/book

* Staging / Production::
 
    $ xdg-open http://<app-server-url>/book

Testing
*******

* Using Vagrant::

     $ fab init_env_vagrant
     $ fab run_tests


More Information 
****************
 
* GitHub : http://github.com/aert/aert-farmerp
* Documentation : http://farmerp.readthedocs.org
 
License 
*******
 
This project is licensed under the MIT license.

Support 
*******
 
* Issue Tracking : https://github.com/aert/aert-farmerp/issues
* Pull Request : https://github.com/aert/aert-farmerp/pulls

Those who wish to contribute directly to the project can contact me at dev.aert@gmail.com to talk about getting repository access granted.


.. _`FAO guidelines`: http://www.fao.org/docrep/field/003/AB619F/AB619F00.htm


