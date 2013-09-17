
Introduction
============

``farm.erp`` is a complete toolbox for agricultural accounting.

Context
*******

.. uml::

   Users -> (Farm ERP System) : Inventory data
   Users -> (Farm ERP System) : Credit Book data
   Users -> (Farm ERP System) : Cash Journal data
   Users -> (Farm ERP System) : Users data
   (Farm ERP System) -> Users : Feedbacks / Previsions / Reportings
    

Global Use Cases
****************

Stackholders
------------

Overview
~~~~~~~~

.. uml::

   :Inventory Manager:
   :Accountant:
   :Director:
   :Admin:

Description
~~~~~~~~~~~

Inventory Manager
    Manages inventory.

Accountant
    Manages credit book and cash journal.

Director
    Same role as ``Inventory Manager`` and ``Accountant`` plus manages user.

Admin
    Same role as Director, plus can manage technical features.

Use case Diagram
----------------

.. uml::

   :Inventory Manager:
   :Accountant:
   :Director:
   :Admin:

