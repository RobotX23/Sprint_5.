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
    PASSWORD_FAIL = By.XPATH, ".//p[@class='input__error text_type_main-default']"
    REGISTER_1 = By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']"
    COME = By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']"
    V_ACCOUNT = By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']"
    PROFILE = By.XPATH, ".//a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive Account_link_active__2opc9']"
    ENTRANCE = By.LINK_TEXT, "Войти"
    RESTORE = By.LINK_TEXT, "Восстановить пароль"
    CONSTRUCTOR = By.LINK_TEXT, "Конструктор"
    STELLEAR_BURGERS = By.XPATH, ".//a[@href='/']"





