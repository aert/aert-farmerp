uc4: Manage inventory
=====================

.. uml::

   ' Manage inventories
   ' ------------------

   'left to right direction
   actor "User" as User


   ' Inventories
   (uc4.10: <b>List inventories</b>)   as (uc4.10) << Project Item >>
   (uc4.11: Add/Edit inventory) as (uc4.11)
   (uc4.12: Delete inventory)   as (uc4.12)
   (uc4.10) <.. (uc4.11) : extends
   (uc4.10) <.. (uc4.12) : extends

   ' Inventory Products
   (uc4.30: <b>List products</b>\n<b>from inventory</b>)    as (uc4.30)
   (uc4.31: Add/Edit product\nfrom inventory) as (uc4.31)
   (uc4.32: Remove product\nfrom inventory)   as (uc4.32)
   (uc4.30) <.. (uc4.31) : extends
   (uc4.30) <.. (uc4.32) : extends

   ' Moves
   (uc4.40: <b>List moves</b>\n<b>from product inventory</b>)     as (uc4.40)
   (uc4.41: Add/Edit move\nfrom product inventory)  as (uc4.41)
   (uc4.42: Delete move\nfrom product inventory) as (uc4.42)
   (uc4.40) <.. (uc4.41) : extends
   (uc4.40) <.. (uc4.42) : extends

   ' Associations
   ' ------------

   User --> (uc4.10)
   User --> (uc4.30)
   User --> (uc4.40)

   (uc4.11) <.. (uc4.30) : extends
   (uc4.31) <.. (uc4.40) : extends

.. toctree::
   :maxdepth: 1

   uc4/uc4-1_inventory_list
   uc4/uc4-2_inventory_manage
   uc4/uc4-3_inventory_manage_product

.. _uc4-reqs:

Requirements
************

#. Only ``Inventory Manager`` can modify content of inventories



