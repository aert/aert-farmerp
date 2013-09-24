
.. _uc1-3:

uc1.3: Edit user
****************

Actors
------

#. Any authenticated user

Preconditions
-------------

1. User is authenticated
2. If user is not in role ``Director`` he must be updating his own account data

Post-conditions
---------------

1. User data is updated
2. If user is ``Director``, system launches :ref:`uc1-1`

Normal flow
-----------

1. User opens the ``Edit user`` screen
2. The system show the new user input form :

   **Data**

   * ``Firstname`` : *string(250), mandatory*
   * ``Surname`` : *string(250), mandatory*
   * ``Email`` : *string(250), mandatory*
   * ``User Roles`` : List of user roles, see :ref:`actors`
   * ``Is Active`` : *Yes/No, default=No*

   **Actions**

   * ``Save``
   * ``Cancel``

3. The user clics on ``Save``
4. The system saves changes for target user 
5. The system displays the following flash message::

    User {{ Email }} updated successfully.

6. End

Alternate flow
--------------

3a. The user clics on ``Cancel``

    1. The system cancels users's input
    2. End

    **Alternate Flow**

    2a. If user is ``Director``

        1. System launches :ref:`uc1-1`

6a. If user is ``Director``

    1. System launches :ref:`uc1-1`

Requirements
------------

1. Only ``Director`` can edit other users data.
2. Only ``Director`` can change ``User Roles`` and ``Is Active``.
3. ``Email`` must be unique in database
