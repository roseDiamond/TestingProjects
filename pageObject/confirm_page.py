from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self,driver):
        self.driver = driver

    # self.driver.find_element(By.ID, "country").send_keys("ind")

    location_field = (By.ID, "country")
    # self.driver.find_element(*ConfirmPage.location_field).send_keys("ind")
    country_name = (By.LINK_TEXT, "India")

    def enter_location_field(self):
        self.driver.find_element(*ConfirmPage.location_field).send_keys("ind")

    def get_country_name(self):
        self.driver.find_element(*ConfirmPage.country_name)


