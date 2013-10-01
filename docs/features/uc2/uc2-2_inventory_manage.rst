
.. _uc2-2:

uc2.2: Manage inventory
***********************

Actors
------

* All authenticated users

Preconditions
-------------

#. User is authenticated
#. User selected an inventory to display

Post-conditions
---------------

#. Inventory data are displayed

Normal flow
-----------

1. The system displays products list :

   **Item Data**

   * ``Designation`` : *string(250), mandatory*
   * ``Quantity`` : *integer, mandatory*

   **Item Actions**

   * ``View Product Inventory``

2. End

Alternate flow
--------------

2.a User clicks ``View Product Inventory``

    1. The system launches :ref:`uc2-3`

Requirements
------------

See :ref:`uc2-reqs`
