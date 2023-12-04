from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome();
# driver.get('http://127.0.0.1:5500/PUK-CIBERSEGURIDAD/python-basics-main/name-main-python/PROYECTO-Buscador/index.html');



# botonAlerta = driver.find_element(By.ID,"alertaSimple");
# botonConfirm = driver.find_element(By.ID,"confirm");
# botonPrompt = driver.find_element(By.ID,"prompt");
# print(botonAlerta,botonConfirm,botonPrompt);
# time.sleep(20);



#driver.switch_to.alert.accept();

"""ALERTA CON CONFIRMACIÓN"""
# botonAlerta = driver.find_element(By.ID,"alertaSimple").click();
# driver.switch_to.alert.accept();     #aceptar alert
# driver.switch_to.alert.dismiss();     # cancelr alert
# driver.switch_to.alert.text;          #para capturar el mensaje de alerta.

"""ALERTA CON PROMPT"""

# driver.switch_to.alert.send_keys("hola desde el alert.");  #enviar texto a un prompt
# driver.switch_to.alert.accept();

driver.get('http:localhost:3000');
driver.implicitly_wait(10);
driver.find_element(By.LINK_TEXT,"Alerts").click();

driver.find_element(By.ID, "buttonAlertSimple").click();
time.sleep(2);
driver.switch_to.alert.accept();



time.sleep(100);
driver.quit();
