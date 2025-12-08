Feature: Login Testing with Scenario Outline

  Scenario Outline: Login test
    Given I open the login page
    When I enter username "<username>" and password "<password>"
    And clicks the login button
    Then the user should be redirected to the dashboard

    Examples:
      | username                 | password     |
      | standard_user            | secret_sauce |
      | locked_out_user          | secret_sauce |
      | problem_user             | secret_sauce |
      | performance_glitch_user  | secret_sauce |
      | error_user               | secret_sauce |
      | visual_user              | secret_sauce |     
      | wrong_user               | secret_sauce |
      | wrong_user               | wrong_pass   |
      | standard_user            | wrong_pass   |
