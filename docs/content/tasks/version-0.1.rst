
Version 0.1
===========

x (A) 2013-10-09 Setup Django +tech @0
**************************************

(A) Setup CSS & Page flows +tech @1
***********************************

(B) Add user management and special user for testing purpose +feature @2
************************************************************************

.. code-block:: gherkin

    Feature: Grant User Access
        As a user
        I want to login
        In order to take actions
    
        Background:
            Given a user named "Abdallah"
            And the system named "Accounting"
            And "Abdallah" is not logged in to "Accounting"

        Scenario: Abdallah logs in
            Given "Abdallah",
            When I launch "Accounting"
            Then I should see the login form

.. code-block:: gherkin

    Feature: User Management
        As an admin
        I want to manage users
        In order to administrate user permissions
    
        Background:
            Given a super user named "admin"
            And "admin" is logged in

        Scenario: Admin manages users
            Given "admin"
            When I open the admin site of "Accounting"
                And I click on "User Management"
            Then I should see the user list
                And I should be allowed to "Add User"
                And I should be allowed to "Del User"
                And I should be allowed to "Update User"

.. code-block:: gherkin

    Feature: Special User for Testing
        As a special user,
        I want a token based connection to the system
        In order to allow automated testing

        Scenario: Special User Activation
            Given I am logged in as "admin"
            When I select a user
                And click on "Generate Token"
            Then the user should be granted password less logins

