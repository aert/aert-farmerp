aert-bookkeeping
''''''''''''''''

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
* Vagrant *(Optional)*


Installation
************
 
* Development::

     $ sudo apt-get install libpq-dev
     $ cdproject
     $ pip install -r deployment/requirements/local.txt
     $ cd sources
     $ add2virtualenv `pwd`

     $ sudo npm install -g less
     $ sudo npm install -g coffee-script

Test
****

* Using Vagrant::

     $ vagrant up
     $ fab dev.h_vagrant dev.setup_ssh_vagrant
     $ cd deploy/ansible
     $ ansible-playbook -i hosts/vagrant top.yml -v


More Information 
****************
 
* GitHub : http://github.com/aert/aert-bookkeeping
* Documentation : https://github.com/aert/aert-bookkeeping/wiki
 
License 
*******
 
This project is licensed under the MIT license.

Support 
*******
 
* Issue Tracking : https://github.com/aert/aert-bookkeeping/issues
* Pull Request : https://github.com/aert/aert-bookkeeping/pulls

Those who wish to contribute directly to the project can contact me at devaert@gmail.com to talk about getting repository access granted.


.. _`FAO guidelines`: http://www.fao.org/docrep/field/003/AB619F/AB619F00.htm

