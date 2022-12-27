from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
driver.get("https://www.udemy.com/join/login-popup/?locale=es_ES&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2F")
driver.maximize_window() #Maximiza el navegador
time.sleep(5)

correo = driver.find_element(By.ID, "email--1")
clave = driver.find_element(By.ID, "id_password")
time.sleep(5)

correo.send_keys("dfdflujogramas@gmail.com")
time.sleep(5)

clave.send_keys("12345678910")
time.sleep(5)

boton = driver.find_element(By.ID, "submit-id-submit")
boton.click()
time.sleep(5)

driver.quit()