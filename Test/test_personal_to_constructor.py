import time

from elements_to_file import TestLocators


class Test:
    def test_personal_to_constructor(self, driver, authorization):
        driver.implicitly_wait(1)
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.V_ACCOUNT).click()
        driver.find_element(*TestLocators.EMAIL).click()
        driver.find_element(*TestLocators.KLICK).send_keys(authorization[0])
        driver.find_element(*TestLocators.PASSWORD).click()
        driver.find_element(*TestLocators.KLICK_PASSWORD).send_keys(authorization[1])
        driver.find_element(*TestLocators.COME).click()
        driver.find_element(*TestLocators.PERSONAL_AREA).click()
        driver.find_element(*TestLocators.CONSTRUCTOR).click()
        assert driver.current_url  == 'https://stellarburgers.nomoreparties.site/'

    def test_personal_to_stellar_burgers(self, driver, authorization):
        driver.implicitly_wait(1)
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.V_ACCOUNT).click()
        driver.find_element(*TestLocators.EMAIL).click()
        driver.find_element(*TestLocators.KLICK).send_keys(authorization[0])
        driver.find_element(*TestLocators.PASSWORD).click()
        driver.find_element(*TestLocators.KLICK_PASSWORD).send_keys(authorization[1])
        driver.find_element(*TestLocators.COME).click()
        driver.find_element(*TestLocators.PERSONAL_AREA).click()
        driver.find_element(*TestLocators.STELLEAR_BURGERS).click()
        assert driver.current_url  == 'https://stellarburgers.nomoreparties.site/'