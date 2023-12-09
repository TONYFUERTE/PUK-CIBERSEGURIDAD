import unittest
from selenium import webdriver
import time
import POM_Xataka

class prueba_pom(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome();
        self.driver.implicitly_wait(20);
        self.driver.get("https://www.google.com");
        # time.sleep(2);

    def test_xataka_primer_articulo(self):

        texto_a_buscar = "xataka";

        #GOOGLE PAGE
        googlePage = POM_Xataka.GooglePage(self.driver);
        googlePage.accept_cookies();
        googlePage.search_for_string(texto_a_buscar);
    

        #SEARCH RESULTS PAGE
        search_results_page = POM_Xataka.SearchResultsPage(self.driver);
        #assert  que retorne un booleano y un texto en caso de fallo. 
        #Lo vamos a implementar en searchResultsPage 
        assert search_results_page.we_are_on_results_page(texto_a_buscar), "No estamos en la página de resultados";
        time.sleep(2);
        search_results_page.click_first_result();

        #XATAKAPAGE
        xakata_page = POM_Xataka.Xataca(self.driver);

        xakata_page.aceptar_cokies_xataka();
        assert "Xataka - Tecnología y gadgets, móviles, informática, electrónica" in xakata_page.get_title()
        xakata_page.primer_articulo();
        title = xakata_page.get_title_primer_articulo();
        print(title);
        # assert "Generar apenas nueve imágenes por IA sale caro. Tanto como recargar..." in title;
        
        # time.sleep(200);
    

    def tearDown(self):
        self.driver.quit();
        
if __name__ == "__main__":
    unittest.main();
        
        
