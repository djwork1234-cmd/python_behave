@login
Feature: Login Functionality

  @smoke
  Scenario: Successful login with valid credentials
    Given the user is on the login page
    When the user enters valid username and password
    And clicks the login button
    Then the user should be redirected to the dashboard

  @regression @negative
  Scenario: Invalid Login
    Given the user is on the login page
    When user enters wrong username and password
    And clicks the login button
    