from selenium.webdriver.common.by import By

class Test_Locators:
    NAME = By.XPATH, ".//label[text()='Имя']"
    KLICK = By.XPATH, "//div[@class='input pr-6 pl-6 input_type_text input_size_default input_status_active']//input[@class='text input__textfield text_type_main-default']"
    EMAIL = By.XPATH, ".//label[text()='Email']"
    PASSWORD = By.XPATH, ".//label[text()='Пароль']"
    KLICK_PASSWORD = By.XPATH, ".//input[@name='Пароль']"

    PERSONAL_AREA = By.XPATH, ".//p[(@class='AppHeader_header__linkText__3q_va ml-2') and (text()='Личный Кабинет')]"
    REGISTER = By.XPATH, ".//a[(@class='Auth_link__1fOlj') and (text()='Зарегистрироваться')]"
    PASSWORD_FAIL = By.XPATH, ".//p[@class='input__error text_type_main-default']"
    REGISTER_1 = By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']"
    COME = By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']"
    V_ACCOUNT = By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']"
    PROFILE = By.XPATH, ".//a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive Account_link_active__2opc9']"
    ENTRANCE = By.XPATH, ".//a[(@class='Auth_link__1fOlj') and (text()='Войти')]"
    RESTORE = By.XPATH, ".//a[(@class='Auth_link__1fOlj') and (text()='Восстановить пароль')]"
    CONSTRUCTOR = By.XPATH, ".//p[(@class='AppHeader_header__linkText__3q_va ml-2') and (text()='Конструктор')]"
    STELLEAR_BURGERS = By.XPATH, ".//a[@href='/']"
    EXID1 = By.XPATH, ".//button[@class='Account_button__14Yp3 text text_type_main-medium text_color_inactive']"
    EXID2 = By.XPATH, ".//div[@class='Auth_login__3hAey']/h2[text()='Вход']"
    EXID = By.XPATH, ".//div[@class='Auth_login__3hAey']/h2"
    BUTTON_FILLING = By.XPATH, ".//div[@class='tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']/span[text()='Начинки']"
    BUTTON_SAUCE = By.XPATH, ".//div[@class='tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']/span[text()='Соусы']"
    BUTTON_BULK = By.XPATH, ".//div[@class='tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']/span[text()='Булки']"
    BUTTON_CONSTRUKTOR = By.XPATH, ".//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']/span"





