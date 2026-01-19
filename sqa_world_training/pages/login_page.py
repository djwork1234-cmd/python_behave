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