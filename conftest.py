import pytest
from selenium import webdriver
import random


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def registr():
    name = ["Света", "Фёдор","Инокентий"]
    random_number = random.randint(100, 200)
    random_name = random.choice(name)
    name = random_name + str(random_number)
    email = random_name + str(random_number) + "@1.ru"
    return name, email

@pytest.fixture(scope='function')
def authorization():
    return "Фродо@1.ru", "123456"