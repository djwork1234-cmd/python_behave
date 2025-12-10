from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys     
import time

@given('I am on the wikipedia homepage')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.wikipedia.org/")
    context.driver.maximize_window()    
    
@when('I search for "selenium(software)"')
def step_impl(context):
    search_box = context.driver.find_element(By.ID, "searchInput")
    search_box.send_keys("selenium (software)")  
    search_box.send_keys(Keys.ENTER)    
    time.sleep(3)  # Wait for the page to load  
    
@then('the page title should contain "selenium"')
def step_impl(context):
    title = context.driver.title
    assert "Selenium"in title, f"Expected 'Selenium' in title but got '{title}'"
    context.driver.quit()   