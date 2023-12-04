import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

class prueba_pon(unittest.TestCase):

    def test_wikipedia_articulo_bueno(self):

        driver = webdriver.Chrome();
        # driver.implicitly_wait(20);
        wait = WebDriverWait(driver, 10, 0.2)

        driver.get("https://www.google.com");
        # time.sleep(2);
        driver.find_element(By.ID,"L2AGLb").click();  #Aceptamos Cookies. 
    
        search_bar = driver.find_element(By.NAME,"q");
        search_bar.send_keys("wikipedia");
        # search_bar.send_keys(Keys.ENTER);
        # time.sleep(2)
        botonBuscarGoogle = (driver.find_element(By.XPATH, "(//input[@value='Buscar con Google'])[2]"))
        botonBuscarEspera = wait.until(EC.element_to_be_clickable(botonBuscarGoogle))
        botonBuscarEspera.click();
        # driver.find_element(By.XPATH, "(//input[@value='Voy a tener suerte'])[2]").click();
        assert "wikipedia - Buscar con Google" in driver.title
        primerElemento = (driver.find_element(By.XPATH, "(//div[@id='search']/descendant::div[@class='g'])[1]/descendant::a[1]"));
        primerEltoEspera = wait.until(EC.element_to_be_clickable(primerElemento));
        primerEltoEspera.click();
        assert "Wikipedia, la enciclopedia libre" in driver.title
        ArticuloBueno = (driver.find_element(By.XPATH,"(//div[@id='Artículo_bueno']/following-sibling::div)[1]/descendant::h2/descendant::a"));
        ArticuloBuenoEspera = wait.until(EC.element_to_be_clickable(ArticuloBueno));
        ArticuloBuenoEspera.click();
        assert "Arrasando - Wikipedia, la enciclopedia libre" in driver.title
        time.sleep(20)
        # time.sleep(100)
        # driver.find_element(By.XPATH, "//button[@class='Tg7LZd']").click();


        # time.sleep(100);

        
        driver.quit()

if __name__ == "__main__":
    unittest.main()