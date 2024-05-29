import time

from elements_to_file import TestLocators


class TestEntrance:
    def test_construktor(self, driver, authorization):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.BUTTON_FILLING).click()
        time.sleep(1)
        assert driver.find_element(*TestLocators.BUTTON_CONSTRUKTOR).text == 'Начинки'
        driver.find_element(*TestLocators.BUTTON_SAUCE).click()
        time.sleep(1)
        assert driver.find_element(*TestLocators.BUTTON_CONSTRUKTOR).text == 'Соусы'
        driver.find_element(*TestLocators.BUTTON_BULK).click()
        time.sleep(1)
        assert driver.find_element(*TestLocators.BUTTON_CONSTRUKTOR).text == 'Булки'



