from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome();
driver.get("http://localhost:3000");

driver.find_element(By.LINK_TEXT,"ShadowDOM").click();

time.sleep(5);

