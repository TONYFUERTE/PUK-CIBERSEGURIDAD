from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class BasePage: 

    def __init__(self, driver):
        self.driver = driver;

    def get_title(self):
        return self.driver.title

class GooglePage(BasePage):

    aceptar_cookies = (By.ID,"L2AGLb");  #Botón de Aceptar Cookies.
    search_bar = (By.NAME,"q");
    botonBuscarGoogle =(By.XPATH, "(//input[@value='Buscar con Google'])[2]")

    # def __init__(self, driver):
    #     self.driver = driver; 

    def accept_cookies(self):
        self.driver.find_element(*self.accept_cookies).click();

    def search_for_string(self, string_to_search):
        searchBar = self.driver.find_element(*self.search_bar);
        searchBar.send_keys(string_to_search);
        self.driver.find_element(*self.botonBuscarGoogle).click();

class SearchResultsPage(BasePage): 

    first_result_Google = (By.XPATH, "((//div[@id='search']/descendant::div[@class='g'])[1]/descendant::a[1]");
    
    # def __init__(self, driver):
    #     self.driver = driver; 

    # def get_title(self):
    #     return self.driver.title;

    def click_first_result(self):
        self.driver.find_element(*self.first_result_Google).click();

    def we_are_on_results_page(self, texto_buscado):
        return str(texto_buscado + " - Buscar con Google") in self.driver.title

class WikipediaPage(BasePage): 

    articulo_bueno = (By.XPATH,"(//div[@id='Artículo_bueno']/following-sibling::div)[1]/descendant::h2/descendant::a"))

    # def __init__(self, driver):
    #     self.driver = driver; 

    def articuloBueno(self):
        self.driver.find_element(*self.articulo_bueno).click();

    def get_title_Art_bueno(self):
    #     return self.driver.title;
        return self.driver.find_element(*self.articulo_bueno).get_attribute("title");

    