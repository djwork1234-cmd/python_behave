Feature: Sauce Demo Login Testing with POM

  Scenario: Successfullogin test with valid credentials
    Given I open the Sauce Demo login page
    When I enter on the sauce-demo webpage username "standard_user" and password "secret_sauce"
    And I click the sauce-demo webpagelogin button
    Then I should see the inventory page 
