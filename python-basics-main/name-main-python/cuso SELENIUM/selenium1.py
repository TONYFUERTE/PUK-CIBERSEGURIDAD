import time

"""Instalación Selenium. Comandos: "pip install -upgrade selenium"  o/y "python -m pip install -upgrade selenium"     """
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service();
options = webdriver.ChromeOptions();
driver = webdriver.Chrome();
driver.get('https://www.wikipedia.org');
print(driver.title);

""""""
#print(driver.find_element(By.TAG_NAME,"title").text); #No lo coge pq no se renderiza en la página.
print(driver.find_element(By.TAG_NAME,"title").get_attribute("textContent"));
print(driver.find_element(By.CLASS_NAME,"central-textlogo-wrapper").text);
print(driver.find_element(By.ID,"js-lang-list-button").text);
print(driver.find_element(By.PARTIAL_LINK_TEXT,"Italiano").text); 

lista = driver.find_elements(By.PARTIAL_LINK_TEXT,"en"); 


# for i in lista:
#     print(i.text);
#print(lista);

listaP = driver.find_elements(By.TAG_NAME,"p")
# print(driver.find_elements(By.TAG_NAME,"p"));
print(len(listaP)); #longitud de la lista

for i in listaP:
    print(f'{i.text} \n');
#print(listaP);

time.sleep(100)

# ...
driver.quit()