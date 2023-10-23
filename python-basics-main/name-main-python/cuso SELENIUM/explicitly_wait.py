from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  #para esperar unas condiciones en concreto
import time

service = Service();
options = webdriver.ChromeOptions();
driver = webdriver.Chrome();
driver.get('https://www.wikipedia.org');


time.sleep(3);
driver.find_element(By.PARTIAL_LINK_TEXT, "Español").click();

wait = WebDriverWait(driver, 10)
#print(driver.find_element(By.PARTIAL_LINK_TEXT, "Invasión rusa de Ucrania" ));
wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Envasión rusa de Ucrania" ))).click();

time.sleep(100);