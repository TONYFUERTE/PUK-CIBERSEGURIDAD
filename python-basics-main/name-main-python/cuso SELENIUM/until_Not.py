from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  #para esperar unas condiciones en concreto
from selenium.common.exceptions import StaleElementReferenceException
import time

service = Service();
options = webdriver.ChromeOptions();
driver = webdriver.Chrome();
driver.get('https://www.wikipedia.org');

time.sleep(3);
driver.implicitly_wait(4);
driver.find_element(By.PARTIAL_LINK_TEXT, "Español").click();

fluent = driver.find_element(By.PARTIAL_LINK_TEXT, "Invasión rusa de Ucrania");

#driver.find_element(By.LINK_TEXT, "Alerts").click();

wait = WebDriverWait(driver, 3, 0.5, (StaleElementReferenceException));
print(wait.until_not(lambda x: fluent.is_selected()));

driver.quit();