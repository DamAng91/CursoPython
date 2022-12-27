from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
driver.get("https://www.udemy.com/join/login-popup/?locale=es_ES&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2F")
time.sleep(1)

usuario = driver.find_element_by_xpath("//input[@id='email--1']")
usuario.send_keys("dfdflujogramas@gmail.com")
time.sleep(1)

clave = driver.find_element_by_xpath("//input[@name='password']")
clave.send_keys("12345678910")
time.sleep(1)

boton = driver.find_element_by_xpath("//input[@name='submit']")
boton.click()
time.sleep(5)

driver.quit()
