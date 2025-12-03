# python_behave
trainining for using pyhton behave with selenium


Install Behave
 pip install behave

Verify instalation and check version
    behave --version
    behave 1.3.3

Install Selenium
 pip install selenium

Verify Selenium
    pipshow selenium
    Name: selenium
Version: 4.38.0
Summary: Official Python bindings for Selenium WebDriver
Home-page: https://www.selenium.dev
Author: 
Author-email: 
License: Apache-2.0
Location: /Users/davidjones/Desktop/training/python_behave_local/.venv_behave/lib/python3.13/site-packages
Requires: certifi, trio, trio-websocket, typing_extensions, urllib3, websocket-client
Required-by: 

Folder Framework:
    Feature files: Where the bdd tests files and step folder is located
        Step Folder : inside the feature folder , where the steps fore the tests are located
            Step files are python files

    Feature files: Are the BDD formated tests in a text format


Running tests
    inside terminal type behave
    % behave
       Scenario: Successful login with valid credentials     # features/login.feature:3
        Given the user is on the login page                 # features/steps/login_steps.py:6 20.671s
        When the user enters valid username and password    # features/steps/login_steps.py:12 0.813s
        And clicks the login button                         # features/steps/login_steps.py:18 2.013s
        Then the user should be redirected to the dashboard # None


    Errored scenarios:
    features/login.feature:3  Successful login with valid credentials

    0 features passed, 0 failed, 1 error, 0 skipped
    0 scenarios passed, 0 failed, 1 error, 0 skipped
    3 steps passed, 0 failed, 0 skipped, 1 undefined
    Took 0min 23.497s