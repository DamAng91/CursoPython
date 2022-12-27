from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
driver.get("https://www.udemy.com/join/login-popup/?locale=es_ES&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2F")
time.sleep(1)

email = driver.find_element_class_name("form-control")
clave = driver.find_element_class_name("textinput")
time.sleep(1)

email.send_keys("damian.angelucci@hotmail.com")
time.sleep(5)

clave.send_keys("holas231")
time.sleep(5)

boton = webdriver.find_element_by_class_name("btn-primary ")
boton.click()
time.sleep(10)


driver.close()
