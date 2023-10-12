import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome()
driver.get('https://www.wikipedia.org')
print(driver.title)

# ...
time.sleep(10)
driver.quit()