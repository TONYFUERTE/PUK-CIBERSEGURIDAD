from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox();
driver.get("http://localhost:3000");
driver.implicitly_wait(10);
usernameLogin = driver.find_element(By.ID,"username");
usernameLogin.send_keys("Pepito");

driver.find_element(By.ID, "password").send_keys("123456");

driver.find_element(By.ID,"loginButton").click();

time.sleep(100);

driver.quit();