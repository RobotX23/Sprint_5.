from selenium.webdriver.common.by import By

class TestLocators:
    NAME = By.XPATH, "//body/div/div/main/div/form/fieldset/div/div/label[text()='Имя']"
    KLICK = By.XPATH, "//div[@class='input pr-6 pl-6 input_type_text input_size_default input_status_active']//input[@class='text input__textfield text_type_main-default']"
    EMAIL = By.XPATH, "//body/div/div/main/div/form/fieldset/div/div/label[text()='Email']"
    PASSWORD = By.XPATH, "//body/div/div/main/div/form/fieldset/div/div/label[text()='Пароль']"
    KLICK_PASSWORD = By.XPATH, "//input[@name='Пароль']"

    BUTTON = By.LINK_TEXT, "Регистрация"
    PERSONAL_AREA = By.LINK_TEXT, "Личный Кабинет"
    REGISTER = By.LINK_TEXT, "Зарегистрироваться"



