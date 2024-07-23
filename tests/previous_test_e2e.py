import time
from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pageObject.checkout_page import CheckOutPage
from pageObject.previous_home_page import HomePage
from utilities.base_class import BaseClass
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# @pytest.mark.usefixtures("setup")
class TestOne(BaseClass):
    def test_e2e(self):
        self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
        home_page = HomePage(self.driver)
        home_page.shopItem().click()

        # cards = self.driver.find_elements(By.CSS_SELECTOR, ".card-title a")
        checkout_page = CheckOutPage(self.driver)
        cards =checkout_page.get_card_titles()
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            print(cardText)
            if cardText == "Blackberry":
                # self.driver.find_elements(By.CSS_SELECTOR, ".card-footer button")[i].click()
                 checkout_page.get_card_footer()[i].click()

        self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        # self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        checkout_page.checkout_item().click()

        self.driver.find_element(By.ID, "country").send_keys("ind")

        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "India")))

        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        # textMatch = self.driver.find_element_by_css_selector("[class*='alert-success']").text
        #
        # assert ("Success! Thank you!" in textMatch)
