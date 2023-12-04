import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import pages

class prueba_pom(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome();
        self.driver.implicity_wait(10);
        self.driver.get("https://www.google.com");
        time.sleep(3);

    def test_wikipedia_articulo_bueno(self):

        texto_a_buscar = "wikipedia";

        #GOOGLE PAGE
        googlePage = pages.GooglePage(self.driver);
        googlePage.accept_cookies();
        googlePage.search_for_string(texto_a_buscar);
    

        #SEARCH RESULTS PAGE
        search_results_page = pages.SearchResultsPage(self.driver);
        #assert  que retorne un booleano y un texto en caso de fallo. 
        #Lo vamos a implementar en searchResultsPage 
        assert search_results_page.we_are_on_results_page(texto_a_buscar), "No estamos en la página de resultados";
        search_results_page.click_first_result();

        #WIKIPEDIAPAGE
        wikipedia_page = pages.WikipediaPage(self.driver);
        assert "Wikipedia, la enciclopedia libre" in wikipedia_page.get_title();

        wikipedia_page.articulo_bueno();
    
        title = wikipedia_page.get_title_Art_bueno();
        assert "Arrasando - Wikipedia, la enciclopedia libre" in title

    def tearDown(self):
        self.driver.quit();
        
        
