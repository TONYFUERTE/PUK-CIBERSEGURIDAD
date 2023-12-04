from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome();
driver.get('http://localhost:3000');

wait = WebDriverWait(driver, 10, 0.2);

driver.find_element(By.PARTIAL_LINK_TEXT,"XPaths").click();

"""Como a veces me da error por no estar cargados los botones le creo una espera específica al
cuadro texto final, tambié se le puede hacer a uno de los botones. """
# boton = (By.TAG_NAME,"button");
# botones_existentes = wait.until(EC.presence_of_all_elements_located(boton));

contenedor = (By.ID,"resultado"); #Tiene que estar dentro de paréntesis para ser una tupla
contenedor_final = wait.until(EC.presence_of_all_elements_located(contenedor));

botones = driver.find_elements(By.TAG_NAME,"button");
# print(len(botones));
print(botones[10].location["y"]);

#Nos desplazamos a la posición del último botón
driver.execute_script("window.scrollBy(0, arguments[0])", botones[10].location["y"]); 

"""Al hacer un switch_to.alert, y aceptarlo ya podemos seguir aplicando Selenium como siempre, ya 
que volvemos al foco, al igual que al ejecutar scripts seguimo en el foco de la página.  """
driver.execute_script("alert('hola!!!!!!')");
time.sleep(2);
driver.switch_to.alert.accept();

time.sleep(50);