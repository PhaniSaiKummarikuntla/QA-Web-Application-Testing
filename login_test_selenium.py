from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com")

username = driver.find_element(By.ID,"user-name")
password = driver.find_element(By.ID,"password")

username.send_keys("standard_user")
password.send_keys("secret_sauce")

driver.find_element(By.ID,"login-button").click()

time.sleep(3)
assert "inventory" in driver.current_url

print("Login test passed")

driver.quit()