from selenium import webdriver

#---------------Before All-----------------
def before_all(context):
    print("=====Test Execution Started=====")
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    
    
    
#---------------After All-----------------
def after_all(context):
    context.driver.quit()
    print("=====Test Execution Completed=====")         
    
    
#---------------Before Scenario-----------------
def before_scenario(context, scenario):
    print(f"-----Starting Scenario: {scenario.name}-----")
    context.driver.get("https://www.wikipedia.org/")
    
    
#---------------After Scenario-----------------
def after_scenario(context, scenario):
    if scenario.status == "failed":
        print(f"-----Scenario Failed: {scenario.name}-----")
        filename = scenario.name.replace(" ", "_") + ".png"
        context.browser.save_screenshot(filename)       
        print(f"Screenshot saved for failed scenario as: {filename}")