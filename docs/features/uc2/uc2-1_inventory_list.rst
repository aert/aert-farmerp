
.. _uc2-1:

uc2.1: List Inventories
***********************

Actors
------

* Inventory Manager

Preconditions
-------------

#. User is authenticated

Post-conditions
---------------

#. All available inventories are displayed
#. Contextual and global actions are displayed according to user's rights

Normal flow
-----------

1. The system displays all available inventories :

   **Item Data**

   * ``Title`` : *string(250), mandatory*
   * ``Start Date`` : *date, mandatory*
   * ``End Date`` : *date*
   * ``Is Completed`` : *Yes/No*.
   * ``Products Count`` : *computed*, number of products inventoried

   **Item Actions**

   * ``View``

   **Global Actions**

   * ``Add Inventory``

2. End

Alternate flow
--------------

2.a User clicks ``View``

    1. The syste launches :ref:`uc2-2`

2.b User clicks ``Add Inventory``

    1. TODO

Requirements
------------

#. If ``Is Completed`` value is ``No``, it's an ``ongoing`` inventory.
#. If user is not ``Inventory Manager`` the only action available is ``View``.

See also :ref:`uc2-reqs`
