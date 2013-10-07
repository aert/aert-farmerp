
uc5: Manage products
====================

.. uml::

   ' Manage products
   ' ---------------

   actor "User" as User

   (uc5.10: <b>List products</b>) as (uc5.10) << Project Item >>

   ' products
   (uc5.11: Add/Edit product) as (uc5.11)
   (uc5.12: Delete product)   as (uc5.12)
   (uc5.10) <.. (uc5.11) : extends
   (uc5.10) <.. (uc5.12) : extends

   ' Associations
   ' ------------

   User     -> (uc5.10)
