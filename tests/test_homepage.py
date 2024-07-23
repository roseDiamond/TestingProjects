import time
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select
from pageObject.home_page import HomePage
from utilities.base_class import BaseClass


class TestHomePage(BaseClass):
    def test_formSubmission(self):
        homepage = HomePage(self.driver)

        homepage.getName().send_keys('sunanda')
        print("suanda sidhharth Gaurav BaharDwaj")
        homepage.getEmail().send_keys('Sunanda123.com')
    

        homepage.getPassword().send_keys('1234')
        homepage.clickCheckBox()

        # Xpath -  //tagname[@attribute='value'] -> //input[@type='submit']
        # CSS -  tagname[attribute='value'] -> //input[@type='submit'],  #id, .classname

        homepage.clickRadiokButton()

        # Static Dropdown
        # dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
        # dropdown.select_by_visible_text("Female")
        # dropdown.select_by_index(0)

        self.selectOptionByText(homepage.getGender(), "Female")
        # dropdown.select_by_value()

        homepage.clickSubmittButton()

        message = homepage.getSucessMessage()
        # print(message)
        assert "Success" in message





