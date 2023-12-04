from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
import time
import pages_POM
    
    
# class Web_testing (unittest.TestCase):

#     def setUp(self):
#         self.driver = webdriver.Chrome();
#         self.driver.get('https://www.google.com');
#         self.driver.implicitly_wait(15);
#         time.sleep(3);
    
#     def test_busqueda_Wikipedia(self):
#         texto_a_buscar = 'Wikipedia'

#         cookies = pages_POM.cookies(self.driver);
#         cookies.Aceptar_Cookies();

#         google = pages_POM.Google(self.driver);
#         google.Escribir_busqueda(texto_a_buscar);
#         assert  texto_a_buscar + " - Buscar con Google" in  google.Obtener_titulo();
#         google.Pulsar_Primer_Elemento();

#         wikipedia = pages_POM.Wikipedia(self.driver);
#         assert "Wikipedia, la enciclopedia libre" in wikipedia.Obtener_titulo();
#         titulo_enlace_Articulo_bueno = wikipedia.titulo_Articulo_bueno();
#         wikipedia.Ir_Articulo_Bueno();
#         assert titulo_enlace_Articulo_bueno + " - Wikipedia, la enciclopedia libre" in wikipedia.Obtener_titulo();

#     def tearDown(self):
#         self.driver.quit();

# if __name__ == "__main__":
#     unittest.main();
    

driver = webdriver.Chrome()
driver.get('https://xataka.com')

print(driver.find_element(By.XPATH, "//div[@class='abstract-content'][1] "))
print(driver.title)













# pages_POM.cookies.Aceptar_Cookiess();





# time.sleep(500);


        
        # self.driver.get("https://www.google.com");
        
#     def test_Articulo_bueno(self):
    
#         self.driver.implicitly_wait(15);

#         self.driver.find_element(By.ID, "L2AGLb").click(); #boton aceptar cookies
#         text_Area = self.driver.find_element(By.ID, "APjFqb"); 
#         text_Area.send_keys("wikipedia");
#         # text_Area.send_keys(Keys.ENTER);

# # #BOTON DE BUSCAR DE GOOGLE
# #         self.driver.find_element(By.XPATH, "(//input[@value='Buscar con Google'])[2]").click();
# #         assert "wikipedia - Buscar con Google" in self.driver.title
# #         time.sleep(3);
# # #ENTRAR EN WIKIPEDIA
# #         self.driver.find_element(By.PARTIAL_LINK_TEXT, "Wikipedia").click();
# #         assert "Wikipedia, la enciclopedia libre" in self.driver.title
# # #ENTRAR EN ARTÍCULO BUENO DE WIKIPEDIA
# #         self.driver.find_element(By.PARTIAL_LINK_TEXT, "Arrasando").click();
# #         assert "Arrasando - Wikipedia, la enciclopedia libre" in self.driver.title

#         time.sleep(5);

#     def tearDown(self):
#         self.driver.quit();

# if __name__ == "__main__":
#     unittest.main();