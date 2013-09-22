
.. _uc1-4:

uc1.4: Delete user
******************

Actors
------

#. Director

Preconditions
-------------

1. User is authenticated
2. User clicked ``Delete`` on :ref:`uc1-1`


Post-conditions
---------------

1. Target user is marked as deleted in database
2. System launches :ref:`uc1-1`

Normal flow
-----------

1. The system show the following confirmation message::

    Delete {{Firstname}} {{Surname}} <{{Email}}> ?

   **Data**

   * ``Firstname`` : Target user's data
   * ``Surname`` : Target user's data
   * ``Email`` : Target user's data

   **Actions**

   * ``Delete``
   * ``Cancel``

2. The user clics on ``Delete``
3. The system marks target user as deleted and launches :ref:`uc1-1` 
4. The system displays the following flash message::

    User {{ Email }} deleted successfully.


Alternate flow
--------------

2a. The user clics on ``Cancel``

    1. The system launches :ref:`uc1-1` 

