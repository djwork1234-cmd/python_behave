Feature: API Testing    
    Scenario: Get a single user
        Given I send a Get request to "https://reqres.in/api/users/2" with api key
        Then the response status code should be 2001
        