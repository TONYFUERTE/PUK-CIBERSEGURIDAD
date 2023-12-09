from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome();
driver.get("http://localhost:3000");
driver.implicitly_wait(10);

driver.find_element(By.PARTIAL_LINK_TEXT, "Radio").click();

# driver.find_elements(By.NAME,"bebida")[0].click();
driver.find_element(By.NAME,"bebida").click();

driver.find_element(By.NAME, "comida2").click();

driver.find_element(By.TAG_NAME,"button").click();

time.sleep(100);
driver.quit();