import time

from elements_to_file import TestLocators


class Test:
    def test_button_exid(self, driver, authorization):
        driver.implicitly_wait(1)
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.V_ACCOUNT).click()
        driver.find_element(*TestLocators.EMAIL).click()
        driver.find_element(*TestLocators.KLICK).send_keys(authorization[0])
        driver.find_element(*TestLocators.PASSWORD).click()
        driver.find_element(*TestLocators.KLICK_PASSWORD).send_keys(authorization[1])
        driver.find_element(*TestLocators.COME).click()
        driver.find_element(*TestLocators.PERSONAL_AREA).click()
        driver.find_element(*TestLocators.EXID1).click()
        assert driver.find_element(*TestLocators.EXID).text == 'Вход'