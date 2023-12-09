from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

driver = webdriver.Chrome();
driver.get("http://localhost:3000");

driver.implicitly_wait(5); #ya que el botón aparece a los 3 segundos.

driver.find_element(By.PARTIAL_LINK_TEXT, "Wait").click();

driver.find_element(By.ID, "implicitWaitButton").click();

wait = WebDriverWait(driver, 10, 0.2);
boton_explicit_wait = (By.ID, "explicitWaitButton");
boton_explicit_wait_elemento = wait.until(EC.element_to_be_clickable(boton_explicit_wait));
boton_explicit_wait_elemento.click();


time.sleep(100);