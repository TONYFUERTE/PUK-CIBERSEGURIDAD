import time

"""Instalación Selenium. Comandos: "pip install -upgrade selenium"  o/y "python -m pip install -upgrade selenium"     """
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service();
options = webdriver.ChromeOptions();
driver = webdriver.Chrome();
driver.get('https://www.wikipedia.org');
time.sleep(1);


#driver.find_element(By.XPATH, "div[@id="search-input"]/descendant::span[text()='Leer'])"  
print(type(driver.find_elements(By.XPATH, "//div[@id='search-input']/descendant::input")))
listaDivId = driver.find_elements(By.XPATH, "//div[@id='search-input']");

print(len(listaDivId));
print(listaDivId);
#print(driver.find_element(By.XPATH, "div[@id='search-input'] input[@id='searchInput']"))

driver.close(); #Cierra sólo la ventana
driver.quit(); #Cierra la ventana y la sesión de selenium