from selenium import webdriver
import time

from elements_to_file import TestLocators

driver = webdriver.Chrome()
driver.maximize_window() # полноэкранный режим


driver.get("https://stellarburgers.nomoreparties.site/")

driver.find_element(*TestLocators.PERSONAL_AREA).click()
time.sleep(1)
driver.find_element(*TestLocators.REGISTER).click()
time.sleep(1)
driver.find_element(*TestLocators.NAME).click()
driver.find_element(*TestLocators.KLICK).send_keys("some_email")
time.sleep(1)
driver.find_element(*TestLocators.EMAIL).click()
driver.find_element(*TestLocators.KLICK).send_keys("some_email")
time.sleep(1)
driver.find_element(*TestLocators.PASSWORD).click()
driver.find_element(*TestLocators.KLICK_PASSWORD).send_keys("some_email")

time.sleep(5)
# Закрой браузер
driver.quit()