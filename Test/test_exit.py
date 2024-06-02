from elements_to_file import Test_Locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import *


class Test_Exit:
    def test_button_exid(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located(Test_Locators.V_ACCOUNT))
        driver.find_element(*Test_Locators.V_ACCOUNT).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located(Test_Locators.RESTORE))
        driver.find_element(*Test_Locators.RESTORE).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located(Test_Locators.ENTRANCE))
        driver.find_element(*Test_Locators.ENTRANCE).click()

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
            expected_conditions.presence_of_element_located(Test_Locators.EXID1))
        driver.find_element(*Test_Locators.EXID1).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located(Test_Locators.EXID))
        assert driver.find_element(*Test_Locators.EXID).text == 'Вход'