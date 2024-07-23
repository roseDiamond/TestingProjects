import time
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select

from TestData.homepageData import HomePageData
from pageObject.home_page import HomePage
from utilities.base_class import BaseClass


class TestHomePage(BaseClass):
    def test_formSubmission(self,getData):
        homepage = HomePage(self.driver)

        homepage.getName().send_keys(getData['namee'])
        homepage.getEmail().send_keys(getData['email'])
        self.selectOptionByText(homepage.getGender(), getData['gender'])
        homepage.getPassword().send_keys(getData['password'])
        homepage.clickCheckBox()

        homepage.clickRadiokButton()
        homepage.clickSubmittButton()
        message = homepage.getSucessMessage()
        assert "Success" in message
        self.driver.refresh()

        # self.driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("helloagain")
        # time.sleep(4)
        # self.driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()

    # data comes from other testdatafile
    @pytest.fixture(params=HomePageData.test_homepage_data)
    def getData(self, request):
        return request.param


    # data pass using dictionary
    # @pytest.fixture(params=[{'namee':'sunanda','email':'sun@123','gender': 'Female','password':1234}, {'namee':'Raju', 'email':'run@123','gender':'Male','password': 12324}])
    # def getData(self, request):
    #     return request.param

    # using tuples
    # @pytest.fixture(params=[('sunanda', 'sun@123', 'Female',1234), ('Raju', 'run@123','Male', 12324), ('rimh', 'sihg@123','Male', 1234)])
    # def getData(self, request):
    #     return request.param
