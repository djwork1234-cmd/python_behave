from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given('the user is on the login page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.saucedemo.com/v1/")
    context.driver.maximize_window()
    
    
@when('the user enters valid username and password')
def step_impl(context):
    context.driver.find_element(By.ID, "user-name").send_keys("standard_user")
    context.driver.find_element(By.ID, "password").send_keys("secret_sauce")
    

@when('clicks the login button')
def step_impl(context):
    context.driver.find_element(By.ID, "login-button").click()
    time.sleep(2)  # Wait for the page to load
    
@then('the user should be redirected to the dashboard')
def step_impl(context):
    title=context.driver.find_element(By.CLASS_NAME, "app_logo").text
    assert title == "Swag Labs", f"Expected 'Swag Labs' but got '{title}'"
    
@when('user enters wrong username and password')
def step_impl(context):
    context.driver.find_element(By.ID, "user-name").send_keys("wrong_username")
    context.driver.find_element(By.ID, "password").send_keys("wrong_password")
    
    
    
    
    
    
@given('I open the login page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.saucedemo.com/v1/")
    context.driver.maximize_window()
    
@when('I enter username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.driver.find_element(By.ID, "user-name").send_keys(username)
    context.driver.find_element(By.ID, "password").send_keys(password)
    
@when('I click the login button')
def step_impl(context):
    context.driver.find_element(By.ID, "login-button").click()
    time.sleep(2)  # Wait for the page to load