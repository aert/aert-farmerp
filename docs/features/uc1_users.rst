uc1: Manage users
=================

.. uml::

   ' Manage users
   ' ------------

   actor "User" as User

   (uc1.1: List users)    as (uc1.1)

   ' Add/Edit user
   (uc1.2: Add/Edit user) as (uc1.2)
   (uc1.21: <b>Manage user rights</b>) as (uc1.21)
   (uc1.2) <.. (uc1.21) : extends

   (uc1.3: Delete user)   as (uc1.3)


   (uc1.1) <.. (uc1.2) : extends
   (uc1.1) <.. (uc1.3) : extends

   User    -> (uc1.1)



.. toctree::
   :maxdepth: 1

   uc1/uc1-1_user_list
   uc1/uc1-2_user_edit
   uc1/uc1-3_user_del


.. Tests
    *****
    
    Administrate user permissions
    -----------------------------
    
    .. code-block:: gherkin
    
        Feature: Administrate user permissions
            In order to administrate user permissions
            As an admin
            I want to manage users
        
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
    
    Grant User Access
    -----------------
    
    .. code-block:: gherkin
    
        Feature: Grant User Access
            In order to test user access
            As a user
            I want to login
        
            Background:
                Given a user named "Abdallah"
                And the system named "Accounting"
                And "Abdallah" is not logged in to "Accounting"
    
            Scenario: Abdallah logs in
                Given "Abdallah",
                When I launch "Accounting"
                Then I should see the login form
    
    Special Testing Account
    -----------------------
    
    .. code-block:: gherkin
    
        Feature: Special User for Testing
            In order to allow automated testing
            As a special user,
            I want a token based connection to the system
    
            Scenario: Special User Activation
                Given I am logged in as "admin"
                When I select a user
                    And click on "Generate Token"
                Then the user should be granted password less logins
