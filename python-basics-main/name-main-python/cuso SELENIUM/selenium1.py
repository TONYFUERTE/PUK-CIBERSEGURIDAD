import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome()
print(driver.title)
driver.get('https://www.wikipedia.org')

# ...
time.sleep(10)
driver.quit()