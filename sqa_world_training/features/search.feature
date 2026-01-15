Feature: Search Functionality

  Scenario: Verify search results page
    Given I am on the wikipedia homepage
    When I search for "selenium(software)"
    Then the page title should contain "seleniumfffffff"