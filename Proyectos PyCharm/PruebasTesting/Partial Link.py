from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
driver.get("https://www.udemy.com/join/login-popup/?locale=en_US&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2F&persist_locale=")
time.sleep(1)

link_recuperacion = driver.find_element_by_partial_link_text("Forgot")
link_recuperacion.click()
time.sleep(5)

correo = driver.find_element_by_id("form-element--1")
correo.send_keys("dfdflujogramas@gmail.com")
time.sleep(1)

validar = driver.find_element_by_class_name("recaptcha-checkbox-border")
validar.click()

boton = driver.find_element_by_class_name("btn-primary")
boton.click()
time.sleep(5)

driver.quit()
