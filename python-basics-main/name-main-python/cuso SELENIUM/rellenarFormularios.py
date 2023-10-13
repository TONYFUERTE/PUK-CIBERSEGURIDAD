from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome();
driver.get('https://www.wikipedia.org');

driver.find_element(By.ID,"searchInput").send_keys("mar");
driver.find_element(By.CLASS_NAME,"pure-button-primary-progressive").click();
print(driver.title);


time.sleep(10);