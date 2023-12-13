from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

drive = webdriver.Chrome();
drive.get("https://infosecmachines.io/");
drive.implicitly_wait(20);

drive.find_element(By.ID, "machinesButtonSearch").send_keys("Medium");
drive.find_element(By.XPATH, "//div[@id='machinesButtonFilter']/following-sibling::button").click();

# time.sleep(5);

sistOpes = drive.find_elements(By.XPATH, "//header/descendant::p[3]");
contador = 1;
for sistOpe in sistOpes:
    sistOpeValor = sistOpe.text;
    print(sistOpeValor);
    if (sistOpeValor == 'Windows'):
        # time.sleep(2);
        # print('entra');
        # drive.find_element(By.XPATH, f"//header[{contador}]/descendant::div[7]").click();
        # header.find_element(B)
    contador = contador + 1;
    if (contador > 26):
        break
    

sistOpes = drive.find_elements(By.XPATH, "//header/descendant::p[4]");
contador = 1;
for sistOpe in sistOpes:
    contador = contador + 1;
    if (contador > 26):
        print(sistOpe.text);




time.sleep(100);