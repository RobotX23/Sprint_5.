import time

from elements_to_file import TestLocators


class Test:
    def test_construktor(self, driver, authorization):
        driver.implicitly_wait(1)
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.BUTTON_FILLING).click()
        assert driver.find_element(*TestLocators.BUTTON_CONSTRUKTOR).text == 'Начинки'
        driver.find_element(*TestLocators.BUTTON_SAUCE).click()
        assert driver.find_element(*TestLocators.BUTTON_CONSTRUKTOR).text == 'Соусы'
        driver.find_element(*TestLocators.BUTTON_BULK).click()
        assert driver.find_element(*TestLocators.BUTTON_CONSTRUKTOR).text == 'Булки'



