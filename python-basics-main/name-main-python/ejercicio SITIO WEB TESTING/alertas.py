from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome();
driver.get("http://localhost:3000");
driver.implicitly_wait(10);

driver.find_element(By.PARTIAL_LINK_TEXT,"Alerts").click();
"""PULSAR ALERTA SIMPLE"""

botonAlerta = driver.find_element(By.ID,"buttonAlertSimple").click();
time.sleep(2);
driver.switch_to.alert.accept();     #aceptar alert simple
time.sleep(3);

"""PULSAR ALERT CONFIRM"""

botonConfirm = driver.find_element(By.ID,"buttonAlertConfirm").click();
time.sleep(2);
driver.switch_to.alert.accept();     #aceptar CONFIRM
botonConfirm = driver.find_element(By.ID,"buttonAlertConfirm").click();
time.sleep(2);
print(driver.switch_to.alert.text);          #para capturar el mensaje de alerta.
driver.switch_to.alert.dismiss();     # cancelr COMFIRM
time.sleep(2);

"""ALERTA CON PROMPT"""

botonConfirm = driver.find_element(By.ID,"buttonAlertPrompt").click();
driver.switch_to.alert.send_keys("hola desde el alert.");  #enviar texto a un prompt
time.sleep(2);
driver.switch_to.alert.accept();

time.sleep(100);
driver.quit();
