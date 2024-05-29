import time

from elements_to_file import TestLocators


class Test:
    def test_registration(self, driver, registr):
        driver.implicitly_wait(1)
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.PERSONAL_AREA).click()
        driver.find_element(*TestLocators.REGISTER).click()
        driver.find_element(*TestLocators.NAME).click()
        driver.find_element(*TestLocators.KLICK).send_keys(registr[0])
        driver.find_element(*TestLocators.EMAIL).click()
        driver.find_element(*TestLocators.KLICK).send_keys(registr[1])
        driver.find_element(*TestLocators.PASSWORD).click()
        driver.find_element(*TestLocators.KLICK_PASSWORD).send_keys("123456")
        driver.find_element(*TestLocators.REGISTER_1).click()
        driver.find_element(*TestLocators.EXID2).click()
        assert driver.find_element(*TestLocators.EXID).text == 'Вход'


    def test_password_error(self, driver, registr):
        driver.implicitly_wait(1)
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.PERSONAL_AREA).click()
        driver.find_element(*TestLocators.REGISTER).click()
        driver.find_element(*TestLocators.NAME).click()
        driver.find_element(*TestLocators.KLICK).send_keys(registr[0])
        driver.find_element(*TestLocators.EMAIL).click()
        driver.find_element(*TestLocators.KLICK).send_keys(registr[1])
        driver.find_element(*TestLocators.PASSWORD).click()
        driver.find_element(*TestLocators.KLICK_PASSWORD).send_keys("12345")
        driver.find_element(*TestLocators.REGISTER_1).click()
        assert driver.find_element(*TestLocators.PASSWORD_FAIL).text == 'Некорректный пароль'
