from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome();
driver.get("http://localhost:3000");

wait = WebDriverWait(driver, 10, 0.2);
cuadroMensaje = (By.ID, "resultado");

cuadroMensaje_espera = wait.until(EC.presence_of_element_located(cuadroMensaje));

driver.find_element(By.LINK_TEXT,"ShadowDOM").click();

# driver.find_element(By.ID,"boton2"); #No puede acceder al boton del shadow

"""Debemos acceder al shadow"""
# time.sleep(2);
nodoShadowhost = driver.find_element(By.ID, "nodoShadowHost");

"""El shadow-root debe estar en estado open para poder acceder, si está en modo 
closed no se podrá acceder."""
nodoShadowRoot = driver.execute_script("return arguments[0].shadowRoot", nodoShadowhost);

print(nodoShadowRoot.find_element(By.ID, "boton2"));  #Ahora ya podemos accedr al botón del shadowDOM
nodoShadowRoot.find_element(By.ID, "boton2").click();

time.sleep(5);

