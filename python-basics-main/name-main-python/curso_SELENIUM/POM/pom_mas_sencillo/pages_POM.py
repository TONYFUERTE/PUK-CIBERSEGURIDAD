from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class Base_a_heredar:

    def __init__ (self, driver):
        self.driver = driver;
        self.title = driver.title;

class cookies(Base_a_heredar): 

    botones = (By.TAG_NAME, "button");

    def Aceptar_Cookies(self):

        for boton in (self.driver.find_elements(*self.botones)):
    
            if(boton.text.find('Aceptar') != -1):
                boton.click();
    
class Google(Base_a_heredar):

    text_area_busqueda = (By.ID, "APjFqb");
    primer_resultado = (By.XPATH, "//div[@id='search']/descendant::div[@class='yuRUbf']/descendant::a[1]")

    def Abrir_Google(self):
        self.driver.get('https://www.google.com');

    def Escribir_busqueda(self, busqueda):
        text_area = self.driver.find_element(*self.text_area_busqueda);
        text_area.send_keys(busqueda);
        text_area.send_keys(Keys.ENTER);
    
    def Obtener_titulo(self):
        return self.driver.title;

    def Pulsar_Primer_Elemento(self):
        self.driver.find_element(*self.primer_resultado).click();
              

class Wikipedia(Base_a_heredar):

    enlace_Articulo_bueno = (By.XPATH,  "//div[@id='Artículo_bueno']/following-sibling::div[1]/descendant::a");

    def Obtener_titulo(self):
        return self.driver.title;

    def titulo_Articulo_bueno(self):
        return self.driver.find_element(*self.enlace_Articulo_bueno).text;

    def Ir_Articulo_Bueno(self):
        self.driver.find_element(*self.enlace_Articulo_bueno).click();


    
    