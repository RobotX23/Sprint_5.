from elements_to_file import Test_Locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Test_constructor:
    def test_construktor_filling(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*Test_Locators.BUTTON_FILLING).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Test_Locators.BUTTON_CONSTRUKTOR))
        assert driver.find_element(*Test_Locators.BUTTON_CONSTRUKTOR).text == 'Начинки'

    def test_construktor_souce(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*Test_Locators.BUTTON_SAUCE).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Test_Locators.BUTTON_CONSTRUKTOR))
        assert driver.find_element(*Test_Locators.BUTTON_CONSTRUKTOR).text == 'Соусы'

    def test_construktor_bulk(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Test_Locators.BUTTON_CONSTRUKTOR))
        assert driver.find_element(*Test_Locators.BUTTON_CONSTRUKTOR).text == 'Булки'






