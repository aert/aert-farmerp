
.. _uc1-1:

uc1.1: List users
*****************

Actors
------

#. Director

Preconditions
-------------

1. User is authenticated

Post-conditions
---------------

1. User list is displayed
2. The ``Add user`` action is available
3. An action list is available for each users displayed

Normal flow
-----------

1. The user opens the users list view
2. The system displays following global actions :

   **Actions:**

   * ``Add user``

3. The system displays the users list.
   For each row: 

   **Data:**     

   * ``Firstname`` : *string(250)*
   * ``Surname`` : *string(250)*
   * ``Email`` : *string(250)*
   * ``User Roles`` : List of user roles, see :ref:`actors`
   * ``Is Active`` : *Yes/No*

   **Actions:**

   * ``Edit``
   * ``Delete``


Alternate flow
--------------

2a. The user clics on ``Add user``

    1. The user clicks on ``Add user``
    2. The system launches :ref:`uc1-2`

3a. The user clics on ``Edit``

    1. The user clicks on ``Edit``
    2. The system launches :ref:`uc1-2`

3b. The user clics on ``Delete``

    1. The user clicks on ``Delete``
    2. The system launches :ref:`uc1-3`


