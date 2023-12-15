from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

drive = webdriver.Chrome();
drive.get("https://infosecmachines.io/");
drive.implicitly_wait(20);

drive.find_element(By.ID, "machinesButtonSearch").send_keys("Medium");
drive.find_element(By.XPATH, "//div[@id='machinesButtonFilter']/following-sibling::button").click();

headers = drive.find_elements(By.XPATH, "//header");
parrafos = drive.find_elements(By.XPATH, "//header/descendant::p");
contador=0;
contadorHeaders=0;
items=[];
contadorWindows=0;
wait = WebDriverWait(drive, 10, (StaleElementReferenceException));

while contador < len(parrafos):
    
    valorParrafo = parrafos[contador].text
    
    if (valorParrafo == 'Linux' or valorParrafo == 'Windows' and contadorHeaders < len(headers)):

        listas = [];
        if (valorParrafo == 'Windows' and contadorWindows < 3):
            contadorWindows = contadorWindows+1;
            
            wait.until(EC.element_to_be_clickable((By.XPATH, "//header[{}]/descendant::div[8]".format(contadorHeaders+1)))).click();
            # wait.until(EC.presence_of_element_located((By.XPATH, "//header[10]/descendant::li")));
            listas = drive.find_elements(By.XPATH, "//header[{}]/descendant::li".format(contadorHeaders+1));
            
            nombreSistema = drive.find_element(By.XPATH, "//header[{}]/descendant::p[1]".format(contadorHeaders+1));
            contadorItems=0;
            items.append("");
            items.append(f"{nombreSistema.text}: Sistema Operativo WINDOWS,  SKILLS: ");
            while contadorItems < len(listas):

                items.append(listas[contadorItems].text);
                contadorItems = contadorItems + 1;
                
            contadorItems = contadorItems + 1;
            
        contadorHeaders = contadorHeaders + 1;
        # print(contadorHeaders);
    contador = contador + 1;

for item in items:
    print(item);

time.sleep(100);