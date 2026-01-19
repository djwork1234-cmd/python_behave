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
    #use the enter_username and enter_password commands from the POM class which get the values from the feature file (When I enter username "standard_user" and password "secret_sauce")
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
    
    