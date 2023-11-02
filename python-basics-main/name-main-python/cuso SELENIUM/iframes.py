from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome();
driver.get('http://localhost:3000');

driver.find_element(By.LINK_TEXT,'iFrames').click();
time.sleep(10)
driver.find_element(By.ID,'inception_1');
# print(driver.find_element(By.CLASS_NAME,'utils_iframe__kQUp4'));




botones = driver.find_element(By.ID,'iframebutton').click();
# print(botones);

time.sleep(50);