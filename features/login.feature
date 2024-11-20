Feature: User login

  Scenario: 001 Successful login with valid credentials
    Given the user is on the login page
    When the user enters valid email and clicks login
    Then the user should be redirected to the registration page

    Scenario: 002 Check if the skip sign in button is working
    Given the user is on the login page
    When the user clicks on the skip sign in button
    Then the user should be redirected to the registration page

