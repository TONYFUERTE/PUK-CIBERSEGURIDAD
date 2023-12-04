import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

class prueba_selenium(unittest.TestCase):


    def setUp(self):
        print('Se ejecuta antes de cada test.');
        self.driver = webdriver.Chrome();
        time.sleep(1);
        self.driver.implicitly_wait(5);
        pass

    def test_a(self):
        print('Se ejecuta en cada test A.');

        """GOOGLE"""

        self.driver.get("https://www.google.com");
        # print(self.driver.title);
        # self.assertEqual("Google", self.driver.title)
        botonRechazarCondiciones = self.driver.find_element(By.CLASS_NAME, "sy4vM");
        # print(botonRechazarCondiciones);
        botonRechazarCondiciones.click();
        searchBar = self.driver.find_element(By.ID, "APjFqb");
        # print(searchBar);
        searchBar.send_keys("wikipedia");
        searchBar.send_keys(Keys.ENTER);
        # buscarConGoogle = self.driver.find_elements(By.CLASS_NAME,"gNO89b");
        # buscarConGoogle[1].click();
   
        """BÚSQUEDA CON GOOGLE"""

        #print(self.driver.find_element(By.XPATH, "//a[@jsname='UWckNb']"));
        self.driver.find_element(By.XPATH, "//a[@jsname='UWckNb']").click();

        """WIKIPEDIA"""
        title = self.driver.title;
        self.assertEqual("Wikipedia, la enciclopedia libre", title);
        time.sleep(4);
        self.driver.back();
        time.sleep(4);
        print(self.driver.current_url);
        
        pass

    # def test_b(self):
    #     print('Se ejecuta en cada test B.');
    #     pass

    def tearDown(self):
        print('Se ejecuta después de cada test.');
        self.driver.quit();
        pass

if __name__ == "__main__":
    unittest.main();