Feature: User registration

  Scenario: 001 Complete the registration form
    Given The user is on registration page
    When Fill the basic details
    Then close the browser