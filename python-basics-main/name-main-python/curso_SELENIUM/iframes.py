from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome();
driver.get('http://localhost:3000');

# driver.find_element(By.LINK_TEXT,'iFrames').click();
driver.find_element(By.PARTIAL_LINK_TEXT,'iFram').click();
time.sleep(3)
# print(driver.find_elements(By.ID,'inception_1'))
# print(driver.find_element(By.CLASS_NAME,'utils_iframe1__kQUp4'));
# iframe1 = driver.find_element(By.CLASS_NAME,'utils_iframe1__kQUp4');
time.sleep(3);
driver.switch_to.frame('inception_1'); #Debe hacerse el switch al iframe a través del ID

botonIFrame = driver.find_element(By.ID,'iframebutton').click()

driver.switch_to.frame('inception_2'); #Debe hacerse el switch al iframe a través del ID
botonIFrame = driver.find_element(By.TAG_NAME,'button').click();
# print(botonIFrame);
time.sleep(3)
driver.switch_to.default_content();
time.sleep(3)

driver.find_element(By.PARTIAL_LINK_TEXT, "Volver").click();

time.sleep(50);