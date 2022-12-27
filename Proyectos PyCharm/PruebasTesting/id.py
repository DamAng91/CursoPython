from selenium import webdriver
import time

controlador = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
controlador.get("https://www.udemy.com/join/login-popup/?locale=es_ES&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2F")
time.sleep(1)

usuario = controlador.find_element_by_id("email--1")
clave = controlador.find_element_by_id("id_password")
time.sleep(1)

usuario.send_keys("dfdflujogramas@gmail.com")
time.sleep(5)

clave.send_keys("12345678910")
time.sleep(5)

boton = controlador.find_element_by_id("submit-id-submit")
boton.click()
time.sleep(5)

controlador.quit()