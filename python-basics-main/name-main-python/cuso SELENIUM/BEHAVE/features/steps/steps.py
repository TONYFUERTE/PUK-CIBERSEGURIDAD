from behave import *
import pages_POM
import time

@given(u'Nos encontramos en google')
def nos_encontramos_en_google(context):
    context.driver.get("https:www.google.com")
    google_page = pages_POM.Google(context.driver)
    accept_cookies = pages_POM.cookies(context.driver)
    accept_cookies.Aceptar_Cookies()
    time.sleep(3)
    
@when(u'Buscamos la cadena \"{texto}\"')
def buscamos_la_cadena(context, texto ):
    google_page = pages_POM.Google(context.driver)
    google_page.Escribir_busqueda(texto)
    
@then(u'La URL del primer resultado es \"{url}\"')
def url_primer_resultado(context, url):
    google_page = pages_POM.Google(context.driver)
    assert url == google_page.get_first_result_url()