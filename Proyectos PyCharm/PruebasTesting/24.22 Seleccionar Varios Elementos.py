from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
driver.get("https://www.udemy.com/join/login-popup/?skip_suggest=1&locale=es_ES&next=https%3A%2F%2Fwww.udemy.com%2F")
driver.maximize_window()

varios = driver.find_elements_by_class_name("form-control")
for i in varios:
    time.sleep(1)
    i.send_keys("holas231")
