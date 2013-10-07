
Overview
========

``farm.erp`` is a complete toolbox for agricultural accounting.

Context
*******

.. uml::

   ' Context
   ' -------

   left to right direction
   [Android] << client >>
   [Web Browser] as Browser << client >>
   usecase System as "
      <b>Farm ERP</b>\n<b>System</b>
      ..
      Inventory
      Cash Journal
      Credit Book
      Users/Projects
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

   ' Stakeholders
   ' ------------

   :Inventory Manager: as Inventory
   :Accountant:
   :Admin:
   :Director:

   Admin     -|> Director
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

Global Use Cases
----------------

.. uml::

   ' Global Use Cases
   ' ----------------

   left to right direction
   :Inventory Manager: as Inventory
   :Accountant:
   ':Admin:
   :Director:
   (uc1: Manage users)           as (guc1)
   (uc2: Manage projects)        as (guc2)
   (uc3: Manage accounts)        as (guc3)
   (uc4: Manage inventory)       as (guc4)
   (uc5: Manage products)        as (guc5)
   (uc6: Manage credit book)     as (guc6)
   (uc7: Manage cash journal)    as (guc7)
   '(uc0: Manage system settings) as (guc0)

   Director --|> Inventory
   Director --|> Accountant
   'Admin     -|> Director

   Director           -> (guc1)
   Director           -> (guc2)
   Director           -> (guc3)
   Inventory         --> (guc4)
   Inventory          -> (guc5)
   Accountant        --> (guc6)
   Accountant         -> (guc7)
   'Admin              -> (guc0)

