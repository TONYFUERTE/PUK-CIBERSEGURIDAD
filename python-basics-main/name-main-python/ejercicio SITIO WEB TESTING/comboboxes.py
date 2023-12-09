from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome();
driver.get("http://localhost:3000");
driver.implicitly_wait(10);

driver.find_element(By.PARTIAL_LINK_TEXT, "Combo").click();

driver.find_element(By.XPATH, "//select[@id='combobox1']//descendant::option[2]").click();

driver.find_element(By.XPATH, "//select[@id='combobox2']//descendant::option[1]").click();
driver.find_element(By.XPATH, "//select[@id='combobox2']//descendant::option[2]").click();

driver.find_element(By.TAG_NAME,"button").click();

time.sleep(100);
driver.quit();