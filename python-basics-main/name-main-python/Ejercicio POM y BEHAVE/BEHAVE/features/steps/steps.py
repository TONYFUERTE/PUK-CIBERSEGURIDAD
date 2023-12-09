from behave import *
import POM_Xataka
import time

@given(u'Nos encontramos en google')
def nos_encontramos_en_google(context):
    context.driver.get("https:www.google.com")
    google_page = POM_Xataka.GooglePage(context.driver)
    google_page.accept_cookies()
    # primer_resultado = POM_Xataka.SearchResultsPage(context.driver)
    # primer_resultado.click_first_result()
    
    
    time.sleep(3)
    
@when(u'Buscamos la cadena \"{texto}\"')
def buscamos_la_cadena(context, texto ):
    google_page = POM_Xataka.GooglePage(context.driver)
    google_page.search_for_string(texto)
    
@then(u'La URL del primer resultado es \"{url}\"')
def url_primer_resultado(context, url):
    google_page = POM_Xataka.SearchResultsPage(context.driver)
    assert url == google_page.get_first_result_url()