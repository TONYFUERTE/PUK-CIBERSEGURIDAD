import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class prueba_pon(unittest.TestCase):

    def test_wikipedia_articulo_bueno(self):

        driver = webdriver.Chrome();
        driver.implicitly_wait(10);

        driver.get("https://www.google.com");
        driver.find_element(By.ID,"L2AGLb").click();
        # aceptarCookies = driver.find_element(By.,"Aceptar todo")
        # print(aceptarCookies);
        search_bar = driver.find_element(By.NAME,"q");
        search_bar.send_keys("wikipedia");
        search_bar.send_keys(Keys.ENTER);

        assert "wikipedia - Buscar con Google" in driver.title
        

        time.sleep(100);


if __name__ == "__main__":
    unittest.main()