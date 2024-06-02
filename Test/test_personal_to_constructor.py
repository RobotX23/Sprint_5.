from elements_to_file import Test_Locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import *

class Test_person_to_constructor:
    def test_personal_to_constructor(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located(Test_Locators.V_ACCOUNT))
        driver.find_element(*Test_Locators.V_ACCOUNT).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located(Test_Locators.EMAIL))
        driver.find_element(*Test_Locators.EMAIL).click()

        driver.find_element(*Test_Locators.KLICK).send_keys(helpers()[0])
        driver.find_element(*Test_Locators.PASSWORD).click()
        driver.find_element(*Test_Locators.KLICK_PASSWORD).send_keys(helpers()[1])
        driver.find_element(*Test_Locators.COME).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located(Test_Locators.PERSONAL_AREA))
        driver.find_element(*Test_Locators.PERSONAL_AREA).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located(Test_Locators.CONSTRUCTOR))
        driver.find_element(*Test_Locators.CONSTRUCTOR).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located(Test_Locators.V_ACCOUNT))
        assert driver.current_url  == 'https://stellarburgers.nomoreparties.site/'

    def test_personal_to_stellar_burgers(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located(Test_Locators.V_ACCOUNT))
        driver.find_element(*Test_Locators.V_ACCOUNT).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located(Test_Locators.EMAIL))
        driver.find_element(*Test_Locators.EMAIL).click()

        driver.find_element(*Test_Locators.KLICK).send_keys(helpers()[0])
        driver.find_element(*Test_Locators.PASSWORD).click()
        driver.find_element(*Test_Locators.KLICK_PASSWORD).send_keys(helpers()[1])
        driver.find_element(*Test_Locators.COME).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located(Test_Locators.PERSONAL_AREA))
        driver.find_element(*Test_Locators.PERSONAL_AREA).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located(Test_Locators.STELLEAR_BURGERS))
        driver.find_element(*Test_Locators.STELLEAR_BURGERS).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located(Test_Locators.V_ACCOUNT))
        assert driver.current_url  == 'https://stellarburgers.nomoreparties.site/'