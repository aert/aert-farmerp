
.. _uc1-2:

uc1.2: Add user
*****************

Actors
------

#. Director

Preconditions
-------------

1. User is authenticated

Post-conditions
---------------

1. New user is added
2. System launches :ref:`uc1-1`

Normal flow
-----------

1. User opens the ``Add user`` screen
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
4. The system adds the new user and launches :ref:`uc1-1` 
5. The system displays the following flash message::

    User {{ Email }} added successfully.



Alternate flow
--------------

3a. The user clics on ``Cancel``

    1. The system cancels users's input and launches :ref:`uc1-1` 

Requirements
------------

1. ``Email`` must be unique in database
