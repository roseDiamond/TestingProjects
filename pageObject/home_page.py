from selenium.webdriver.common.by import By

from pageObject.checkout_page import CheckOutPage

# self.driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Rahul")
# self.driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
# self.driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
# self.driver.find_element(By.ID, "exampleCheck1").click()




class HomePage:
    def __init__(self, driver):
        self.driver = driver
    shop = (By.CSS_SELECTOR,  "a[href*='shop']")
    name = (By.XPATH, "//input[@name='name']")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkbox = (By.ID, "exampleCheck1")
    radiobutton =(By.CSS_SELECTOR, "#inlineRadio1")
    submittbutton =(By.XPATH, "//input[@type='submit']")
    message =(By.CLASS_NAME, "alert-success")
    gender = (By.ID, "exampleFormControlSelect1")

    def shopItem(self):
        self.driver.find_element(*HomePage.shop).click()
        return CheckOutPage(self.driver)

    def getName(self):
        return self.driver.find_element(*HomePage.name)
    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def clickCheckBox(self):
        self.driver.find_element(*HomePage.checkbox).click()

    def clickRadiokButton(self):
        self.driver.find_element(*HomePage.radiobutton).click()

    def clickSubmittButton(self):
        self.driver.find_element(*HomePage.submittbutton).click()

    def getSucessMessage(self):
        return self.driver.find_element(*HomePage.message).text

    def  getGender(self):
        return self.driver.find_element(*HomePage.gender)





        # return checkoutPage