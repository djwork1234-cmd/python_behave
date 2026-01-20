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


Hooks
    Create a or add to environment.py file in the features folder the following:
        Different hooks:
            before_all - the config will run before all tests executions start i.e open browser
                def before_all(context):
                    print("=====Test Execution Started=====")
                    context.driver = webdriver.Chrome()
                    context.driver.maximize_window()
            after_all - the config will run before all tests executions Finished i.e close browser
                def after_all(context):
                    context.driver.quit()
                    print("=====Test Execution Completed=====")   
            before_scenario - the config will run before all tests  scenario executions start 
                def before_scenario(context, scenario):
                    print(f"-----Starting Scenario: {scenario.name}-----")
                    context.driver.get("https://www.wikipedia.org/")
            after_scenario - the config will run after all tests  scenario executions start i.e failure screenshot
                def after_scenario(context, scenario):
                    if scenario.status == "failed":
                        filename = scenario.name.replace(" ", "_") + ".png"
                        context.browser.save_screenshot(filename)       
                        print(f"Screenshot saved for failed scenario as: {filename}")

Page Object Model (POM)
    Within your web app’s UI, there are areas where your tests interact with. A Page Object only models these as objects within the test code. This reduces the amount of duplicated code and means that if the UI changes, the fix needs only to be applied in one place.

    Page Object Model is a Design Pattern that has become popular in test automation for enhancing test maintenance and reducing code duplication. A page object is an object-oriented class that serves as an interface to a page of your AUT. The tests then use the methods of this page object class whenever they need to interact with the UI of that page. The benefit is that if the UI changes for the page, the tests themselves don’t need to change, only the code within the page object needs to change. Subsequently, all changes to support that new UI are located in one place

    Create a pages directory within the projects folder
        Scructure
            - Project folder i.e sqa_world_training
                - features
                    - steps folder
                    - feature files
                - pages
                    - POM files
                - data folder
                    - data files i.e login_data.xlsx

    Create a feature file
        Feature: Sauce Demo Login Testing with POM

             Scenario: Successfullogin test with valid credentials
               Given I open the Sauce Demo login page
               When I enter username "standard_user" and password "secret_sauce"
               And I click the login button
               Then I should see the inventory page 

    Create a POM python file within the pages directory i.e login_page.py
        from selenium.webdriver.common.by import By     

        class LoginPage:
            #define the following
            #the web site URL
            URL="https://www.saucedemo.com/v1/"
            #user name text field on the web page (Found by the ID)
            USERName_INPUT = (By.ID, "user-name")
            #password text field on the web page (Found by the ID)
            PASSWORD_INPUT = (By.ID, "password")
            #login button on the web page (Found by the ID)
            LOGIN_BUTTON = (By.ID, "login-button")
            #inventory page is displayed on the web page (Found by the ID)
            INVENTORY_CONTAINER = (By.ID, "inventory_container")

            def __init__(self, driver):
                self.driver = driver        

            #command to open the webpage using the URL above (https://www.saucedemo.com/v1/)
            def open(self):
                self.driver.get(self.URL)

            #command to enter the username (the username value is the username defined in the feature file : When I enter username "standard_user")
            def enter_username(self, username):
                self.driver.find_element(*self.USERName_INPUT).send_keys(username)  #username value is standard_user

            #command to enter the password (the password value is the password defined in the feature file : When I enter password "secret_sauce")
            def enter_password(self, password):
                self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)  #password value is secret_sauce

            #command to click the login button
            def click_login(self):
                self.driver.find_element(*self.LOGIN_BUTTON).click()

            #command to check if the inventory page is displayed
            def is_inventory_page_displayed(self):
                return self.driver.find_element(*self.INVENTORY_CONTAINER).is_displayed()


    Create a step python file within the steps directory/folder i.e login_pom_steps.py
        #import behave commands
        from behave import given, when, then
        #import the webdriver from selenium
        from selenium import webdriver
        #import the LoginPage class from the pages folder
        from pages.login_page import LoginPage     
        
        @given('I open the Sauce Demo login page')
        def step_open_login_page(context):
            #use a chrome driver
            context.driver = webdriver.Chrome()
            #use the URL input from the pages.login_page POM class to open the web page
            context.login_page = LoginPage(context.driver)
            #use the the web page using the open command from the POM class
            context.login_page.open()
        
        @when('I enter on the sauce-demo webpage username "standard_user" and password "secret_sauce"')
        def step_enter_credentials(context, username, password):
            #use the enter_username and enter_password commands from the POM class which get the values from the feature file (When I enter username        "standard_user" and password "secret_sauce")
            context.login_page.enter_username(username)
            context.login_page.enter_password(password)
            
        @when('I click the sauce-demo webpagelogin button')
        def step_click_login(context):
            #use the click_login command from the POM class
            context.login_page.click_login()    
            
        @then('I should see the inventory page')
        def step_verify_inventory_page(context):
            #use the is_inventory_page_displayed command from the POM class to verify the inventory page is displayed
            assert context.login_page.is_inventory_page_displayed(), "Inventory page is not displayed" 
            #close the browser
            context.driver.quit()
    
 API Testing
    Istallation: pip install behave requests
    Test website: https://reqres.in/#how

    Create a new feature file i.e API.feature
        Feature: API Testing    
            Scenario: Get a single user
                Given I send a Get request to "https://reqres.in/api/users/2" with api key
                Then the response status code should be 200

    Create a Step pyhton file i.e API_steps.py
        import requests
        from behave import given, then

        API_KEY = "regres-free-v1"
        # Set up headers with the API key
        HEADERS = {"x-api-key": API_KEY}

        # Step definition to send a GET request with API key in headers
        @given('I send a Get request to "{url}" with api key')
        def step_send_get_request_with_api_key(context, url):
            context.response = requests.get(url, headers=HEADERS)       
            #print reponse body in a console
            print("\n==== Response Body ====")
            print(context.response.text)

        # Step definition to check the response status code should be 200
        @then('the response status code should be {status_code:d}')
        def step_check_response_status_code(context, status_code):
            #Assert that the API returned the expected status code
            assert context.response.status_code == status_code, \
                f"Expected status code {status_code}, but got {context.response.status_code}"


    Execution Code: behave --no-capture features/API.feature
    Result : 
            USING RUNNER: behave.runner:Runner
            Feature: API Testing # features/API.feature:1

              Scenario: Get a single user                                                  # features/API.feature:2
                Given I send a Get request to "https://reqres.in/api/users/2" with api key # features/steps/API_steps.py:9

            ==== Response Body ====
            {"data":{"id":2,"email":"janet.weaver@reqres.in","first_name":"Janet","last_name":"Weaver","avatar":"https://reqres.in/img/faces/2-image.jpg"},"support":{"url":"https://           contentcaddy.io?utm_source=reqres&utm_medium=json&utm_campaign=referral","text":"Tired of writing endless social media content? Let Content Caddy generate it for you."},       "_meta":{"powered_by":"ReqRes","docs_url":"https://app.reqres.in/documentation","upgrade_url":"https://app.reqres.in/upgrade","example_url":"https://app.reqres.in/examples/        notes-app","variant":"v1_a","message":"Classic ReqRes still works. Projects add persistence, auth, and logs.    Given I send a Get request to "https://reqres.in/api/users/2"          with api key # features/steps/API_steps.py:9 0.173s
                Then the response status code should be 200                                # features/steps/API_steps.py:17 0.000s

            1 feature passed, 0 failed, 0 skipped
            1 scenario passed, 0 failed, 0 skipped
            2 steps passed, 0 failed, 0 skipped
            Took 0min 0.174s

    Failed Result:
            USING RUNNER: behave.runner:Runner
            Feature: API Testing # features/API.feature:1
            
              Scenario: Get a single user                                                  # features/API.feature:2
                Given I send a Get request to "https://reqres.in/api/users/2" with api key # features/steps/API_steps.py:9
            
            ==== Response Body ====
            {"data":{"id":2,"email":"janet.weaver@reqres.in","first_name":"Janet","last_name":"Weaver","avatar":"https://reqres.in/img/faces/2-image.jpg"},"support":{"url":"https://           contentcaddy.io?utm_source=reqres&utm_medium=json&utm_campaign=referral","text":"Tired of writing endless social media content? Let Content Caddy generate it for you."},       "_meta":{"powered_by":"ReqRes","docs_url":"https://app.reqres.in/documentation","upgrade_url":"https://app.reqres.in/upgrade","example_url":"https://app.reqres.in/examples/        notes-app","variant":"v1_a","message":"Classic ReqRes still works. Projects add persistence, auth, and logs.    Given I send a Get request to "https://reqres.in/api/users/2"          with api key # features/steps/API_steps.py:9 0.190s
                Then the response status code should be 2001                               # features/steps/API_steps.py:17 0.000s
                  ASSERT FAILED: Expected status code 2001, but got 200
            
            
            
            Failing scenarios:
              features/API.feature:2  Get a single user
            
            0 features passed, 1 failed, 0 skipped
            0 scenarios passed, 1 failed, 0 skipped
            1 step passed, 1 failed, 0 skipped
            Took 0min 0.190s

Use Excelsheets for test data
    Installation
        web page: https://pypi.org/project/openpyxl/
        Pip installation command: pip install openpyxl
    Create a or add to environment.py file in the features folder the following:
        import openpyxl

        def_before_all_data(context)
        # add the path to the excel sheet to be opened 
            workbook = openpyxl.load_workbook('/Users/davidjones/Desktop/training/python_behave_local/python_behave/sqa_world_training/login_data.xlsx')
        #get the active worksheet
            sheet = workbook.active
        # store all data into an empty list
            context.users = []
        # ignore the headers(first row) of the excel sheet
            headers = [cell.value for cell in sheet[1]]
            for row in sheet.iter_rows(min_row=2, values_only=True):
                data = dict(zip(headers, row))
                context.users.append(data)
    Create a Feature file
        Feature: Loginfunctionality with Excel Data

        Scenario: Login using credentials from Excel
        Given I open the login page
        When I login with users from Excel

    Create a steps file
        login_steps.py
            from unittest.mock import Base
            from behave import given, when, then
            from selenium import webdriver
            from selenium.webdriver.common.by import By
            import time
            Base_URL = "https://practicetestautomation.com/practice-test-login/"


            @given("I open the test login page")
            def step_open_login_excel(context):
                context.driver = webdriver.Chrome()
                context.driver.maximize_window()
                context.driver.get(Base_URL)

            @when("I login with users from Excel")
            def step_impl_excel(context):
                for user in context.users:
                    context.driver.get(Base_URL)

                    username = user['username']
                    password = user['password']

                    username_locator = (By.ID, "username")
                    password_locator = (By.ID, "password")
                    login_button_locator =(By.ID, "submit")

                    time.sleep(2)

                    context.driver.find_element(*username_locator).send_keys(username)
                    context.driver.find_element(*password_locator).send_keys(password)
                    context.driver.find_element(*login_button_locator).click()
                    time.sleep(2)  # Wait for the page to load

Parallel Executions
    Able to multiple tests within a feature file at the same time, instaed of one after another
    Installation:
        pip install behavex
    Check Version
        behavex --version
            BehaveX 4.6.0
            Exit code: 0
        
    Execution Code
        behavex login.feature  --parallel-processes 2 --parallel-scheme scenario
            behavex - to use behavex not just normal behave package
            login.feature - the feature file to be tested
             --parallel-processes 2 - the number of workers to be used for testing
             --parallel-scheme scenario - 

HTML-pretty-formater report

    Creates a test result report which can shown in a browser

    Installation:
        web page: https://pypi.org/project/behave-html-pretty-formatter/
        Pip installation command: python3 -m pip install behave-html-pretty-formatter
        Create behave.ini file within the project folder and copy and save the code displayed on the web page


    Create Report
        command: behave search.feature -f behave_html_pretty_formatter:PrettyHTMLFormatter -o reports/report.htmlbehave-html-pretty-formatter
            search.feature - test file to be tested
            -f behave_html_pretty_formatter:PrettyHTMLFormatter - to format the report into pretty html formatter
            -o - cammand to open a folder
            reports - folder to open or create
            report.html - report name

        Open the report (Vs code and mac)
        Right click on the report file in the report folder
        Select copy path
        Open a broswer
        Paste and go the copied path
        Report is displayed

Allure Reports
 <--------To Be added at a later date--------->