Feature: Comprobar la direccion web
Descripcion de la feature actual. 

    Scenario: La URL es correcta
        Given Nos encontramos en google
        When Buscamos la cadena "xataka"
        Then La URL del primer resultado es "https://www.xataka.com/"