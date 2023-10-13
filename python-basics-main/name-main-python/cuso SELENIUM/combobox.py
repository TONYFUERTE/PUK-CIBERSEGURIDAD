from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome();
driver.get('http://127.0.0.1:5500/index.html');
#driver.find_element(By.ID, "marca").click()

select = Select(driver.find_element(By.ID, "marca"))
#time.sleep(3);
#select.select_by_index(1);
# select.select_by_index(1);
# select.select_by_index(2);
# select.select_by_index(3);

# select.select_by_value("Ford");

select.select_by_visible_text('Dodge');

#print(select.options);

for i in select.options:
    print(i.text);
    # print(i.get_attribute("value"));

print(driver.find_elements(By.ID, "transmision"));
select2 = Select(driver.find_element(By.ID, "transmision"));

select2.select_by_value("automatico")

time.sleep(5);
print(driver.find_element(By.ID, "resultado"));
#print(driver.find_element(By.ID, "resultado").text);
selectResultado = driver.find_element(By.ID, "resultado");


time.sleep(10);

driver.quit();