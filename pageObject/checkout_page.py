from selenium.webdriver.common.by import By

from pageObject.confirm_page import ConfirmPage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    card_title = (By.CSS_SELECTOR, ".card-title a")
    card_footer = (By.CSS_SELECTOR, ".card-footer button")
    checkoutItem = (By.XPATH, "//button[@class='btn btn-success']")
    # checkout = (By.XPATH, "//button[@class='btn btn-success']")


    def get_card_titles(self):
        return self.driver.find_elements(*CheckOutPage.card_title)

    # self.driver.find_elements(By.CSS_SELECTOR, ".card-footer button")[i].click()f

    def get_card_footer(self):
        return self.driver.find_elements(*CheckOutPage.card_footer)



    def checkout_item(self):
        self.driver.find_element(*CheckOutPage.checkoutItem).click()
        confirm_page = ConfirmPage(self.driver)
        return confirm_page
