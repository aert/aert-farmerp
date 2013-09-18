
Introduction
============

``farm.erp`` is a complete toolbox for agricultural accounting.

Context
*******

.. uml::

   left to right direction
   Users --> (Farm ERP \nSystem) : Inventory data
   Users --> (Farm ERP \nSystem) : Credit Book data
   Users --> (Farm ERP \nSystem) : Cash Journal data
   Users --> (Farm ERP \nSystem) : Users data
   (Farm ERP \nSystem) ...> Users : Feedbacks \nPrevisions \nReportings
    

Global Use Cases
****************

Stackholders
------------

Overview
~~~~~~~~

.. uml::

   :Inventory Manager:
   :Accountant:
   :Director: -|> :Inventory Manager:
   :Director: -|> :Accountant:
   :Admin: -|> :Director:

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

