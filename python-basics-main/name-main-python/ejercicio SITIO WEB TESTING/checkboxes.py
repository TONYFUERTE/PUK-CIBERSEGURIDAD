from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome();
driver.get("http://localhost:3000");

driver.find_element(By.PARTIAL_LINK_TEXT, "Check").click();
time.sleep(3);
listaCompra = driver.find_elements(By.TAG_NAME,"input");
listaCompra[0].click();
listaCompra[2].click();
print(len(listaCompra));

time.sleep(100);




driver.quit();