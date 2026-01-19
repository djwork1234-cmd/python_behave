import openpyxl
from selenium import webdriver



#---------------Before All-----------------
def before_all(context):
    print("=====Test Execution Started=====")
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
 
def before_all(context):
    # Load Excel data before all tests
    workbook = openpyxl.load_workbook("/Users/davidjones/Desktop/training/python_behave_local/python_behave/sqa_world_training/login_data.xlsx")
    sheet = workbook.active
    context.users = []
    
    headers = [cell.value for cell in sheet[1]]
    for row in sheet.iter_rows(min_row=2, values_only=True):
        data = dict(zip(headers, row))
        context.users.append(data)
  
    
"""
 
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
        filename = scenario.name.replace(" ", "_") + ".png"
        context.browser.save_screenshot(filename)       
        print(f"Screenshot saved for failed scenario as: {filename}")
"""