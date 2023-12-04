from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service();
options = webdriver.ChromeOptions();
driver = webdriver.Chrome();
driver.get('https://www.wikipedia.org');

driver.implicitly_wait(5); #Esperará durante 5 segundos haciendo las peticiones necesarias


driver.find_element(By.PARTIAL_LINK_TEXT, "Español").click();
# time.sleep(5);

#print(driver.find_elements(By.PARTIAL_LINK_TEXT, "Leer"));
driver.find_element(By.PARTIAL_LINK_TEXT, "Bienvenidos").click();
time.sleep(100);