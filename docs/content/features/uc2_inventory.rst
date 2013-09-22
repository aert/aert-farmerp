
uc2: Manage inventory
=====================

.. uml::

   left to right direction
   actor "Inventory Manager" as Inventory


   rectangle "Manage Inventory" {
      (uc2.1: List inventories)  as (uc2.1)
      (uc2.2: Add inventory)    as (uc2.2)
      (uc2.3: Edit inventory) as (uc2.3)
      (uc2.4: Delete inventory) as (uc2.4)

      Inventory --> (uc2.1)
      Inventory --> (uc2.2)
      Inventory --> (uc2.3)
      Inventory --> (uc2.4)

   }
   

**Child use cases:**

.. toctree::
   :maxdepth: 1

   uc2/uc2-1_inventory_list
   uc2/uc2-2_inventory_add
   uc2/uc2-3_inventory_edit
   uc2/uc2-4_inventory_del

