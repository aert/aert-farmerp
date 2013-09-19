
Overview
========

``farm.erp`` is a complete toolbox for agricultural accounting.

Context
*******

.. uml::

   left to right direction
   [Android] << client >>
   [Web Browser] as Browser << client >>
   usecase System as "
      <b>Farm ERP</b>\n<b>System</b>
      ..
      Inventory
      Cash Journal
      Credit Book
      Users
   "

   Users   <--> Android
   Users   <--> Browser 

   Android <--> (System) 
   Browser <--> (System)

Global Use Cases
****************

.. _actors:

Stakeholders
------------

.. uml::

   :Inventory Manager: as Inventory
   :Accountant:
   :Admin:
   :Director:

   Admin    -|>  Director
   Director --|> Inventory
   Director --|> Accountant

**Inventory Manager**
    Manages inventory.

**Accountant**
    Manages credit book and cash journal.

**Director**
    Same role as ``Inventory Manager`` and ``Accountant`` plus manages user.

**Admin**
    Same role as Director, plus can manage technical features.

Use Cases
---------

.. uml::

   :Inventory Manager: as Inventory
   :Accountant:
   :Admin:
   :Director:
   (uc0: Manage system settings) as (guc0)
   (uc1: Manage users) as (guc1)
   (uc2: Manage inventory) as (guc2)
   (uc3: Manage credit book) as (guc3)
   (uc4: Manage cash journal) as (guc4)

   Admin    -|>  Director
   Director --|> Inventory
   Director --|> Accountant

   Admin      -> (guc0)
   Director   -> (guc1)
   Inventory  -> (guc2)
   Accountant --left--> (guc3)
   Accountant --right--> (guc4)


