
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

   **Data**

   * ``Title`` : *string(250), mandatory*
   * ``Start Date`` : *date, mandatory*
   * ``End Date`` : *date*
   * ``Is Completed`` : *Yes/No*.

   **Actions**

   * ``View``
   * ``Edit``

Alternate flow
--------------


Requirements
------------

#. If ``Is Completed`` value is ``No``, it's an ``ongoing`` inventory (see :ref:`uc2-1a`).
#. Only ``Inventory Manager`` can launch ``Edit`` action.

See also :ref:`uc2-reqs`
