from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox();
driver.get('http://127.0.0.1:5500/PUK-CIBERSEGURIDAD/python-basics-main/name-main-python/PROYECTO-Buscador/index.html');

time.sleep(10);

driver.quit();