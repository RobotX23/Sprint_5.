from elements_to_file import Test_Locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Test_registration:
    def test_registration(self, driver, registr):
        driver.get("https://stellarburgers.nomoreparties.site/")
        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located(Test_Locators.PERSONAL_AREA))
        driver.find_element(*Test_Locators.PERSONAL_AREA).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located(Test_Locators.REGISTER))
        driver.find_element(*Test_Locators.REGISTER).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located(Test_Locators.NAME))
        driver.find_element(*Test_Locators.NAME).click()
        driver.find_element(*Test_Locators.KLICK).send_keys(registr[0])
        driver.find_element(*Test_Locators.EMAIL).click()
        driver.find_element(*Test_Locators.KLICK).send_keys(registr[1])
        driver.find_element(*Test_Locators.PASSWORD).click()
        driver.find_element(*Test_Locators.KLICK_PASSWORD).send_keys("123456")

        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located(Test_Locators.REGISTER_1))
        driver.find_element(*Test_Locators.REGISTER_1).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located(Test_Locators.EXID2))
        driver.find_element(*Test_Locators.EXID2).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located(Test_Locators.EXID))
        assert driver.find_element(*Test_Locators.EXID).text == 'Вход'


    def test_password_error(self, driver, registr):
        driver.get("https://stellarburgers.nomoreparties.site/")
        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located(Test_Locators.PERSONAL_AREA))
        driver.find_element(*Test_Locators.PERSONAL_AREA).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located(Test_Locators.REGISTER))
        driver.find_element(*Test_Locators.REGISTER).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located(Test_Locators.NAME))
        driver.find_element(*Test_Locators.NAME).click()
        driver.find_element(*Test_Locators.KLICK).send_keys(registr[0])
        driver.find_element(*Test_Locators.EMAIL).click()
        driver.find_element(*Test_Locators.KLICK).send_keys(registr[1])
        driver.find_element(*Test_Locators.PASSWORD).click()
        driver.find_element(*Test_Locators.KLICK_PASSWORD).send_keys("12345")

        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located(Test_Locators.REGISTER_1))
        driver.find_element(*Test_Locators.REGISTER_1).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located(Test_Locators.PASSWORD_FAIL))
        assert driver.find_element(*Test_Locators.PASSWORD_FAIL).text == 'Некорректный пароль'
