import unittest
import platform
import tests2 

class Mis_tests(unittest.TestCase):

    sumando1 = 0;
    sumando2 = 0;
    ejecutar = True;

    # @classmethod
    # def setUpClass(cls):
    #     print('Cargando entorno.');
    #     print('Cargado.');
    #     print('Cargando Base de datos.');

    def setUp(self):
        self.sumando1 = 2;
        self.sumando2 = 2;
        if self.sumando1 + self.sumando2 >= 10: self.ejecutar = False;
    
    @unittest.skip('No se ejecuta hasta que se realicen los cambios necesarios. ') #Evita que se ejecute el siguiente test. 

    def test_suma(self):
    #    self.assertTrue(self.correr, 'Correr No es True');       # con que falle una de las condiciones ya toma como fallido el test
        self.assertEqual(self.sumando1 + self.sumando2, 4, 'No se cumple el test suma.');
    
    @unittest.skip('No se ejecuta hasta que se realicen los cambios necesarios. ')

    def test_resta(self):
        self.assertTrue(self.sumando1 - self.sumando2==0, 'No se cumple el test resta.');
    
    @unittest.skipIf(platform.system() == 'Windows', 'No se ejecuta en Windows.')
    # @unittest.skipIf(platform.system() == 'Linux', 'No se ejecuta en Linux.')
    
    def test_verifica_si_falso(self):
        self.assertFalse(self.sumando1==0, 'False esperado')

    @unittest.skipUnless(platform.system() == 'Linux','Sólo se ejecuta en Linux ')
    
    def test_ejecutar(self):
        self.assertTrue(self.ejecutar, 'Ejecutar No es True');
    
    def test_noEqual(self):
        self.assertNotEqual(self.ejecutar, self.sumando1);
    
    def test_es_nulo(self):
        a=None;
        self.assertIsNone(a,'No escribe nada.');
    
    def test_no_es_nulo(self):
        a=0;
        self.assertIsNotNone(a,'No debería ser None');
    
    def test_is(self):
        a=5;
        b=5;    #Float y int no so n el mismo tipo

        # if a is b: print(f'{a} y {b} Son iguales para el is')
        # else: print(f'{a} y {b} No son iguales para el is. Diferente tipo');

        # if a == b: print(f'{a} y {b} Son iguales con ==')
        # else: print(f'{a} y {b} No son iguales para el ==. Diferente tipo');

        self.assertIs(a,b,'No son iguales para el is.');
    
    def test_IsNot(self):
        a=5;
        b=5.0;
        self.assertIsNot(a,b,'Son iguales. ')

    def test_text_In(sefl):
        a='Hola';
        b='Hola Mundo';
        sefl.assertIn(a,b,"El texto no está incluido");
    
    def test_text_NotIn(sefl):
        a='Adios';
        b='Hola Mundo';
        sefl.assertNotIn(a,b,"El texto está incluido");
    
    def test_Greater(sefl):
        a=7;
        b=5;
        sefl.assertGreater(a,b,"A debe ser mayor que B.");
    
    def test_GreaterEqual(sefl):
        a=7;
        b=5;
        sefl.assertGreaterEqual(a,b,"A debe ser mayor o igual que B.");
    
    def test_Less(sefl):
        a=4;
        b=5;
        sefl.assertLess(a,b,"A debe ser menor que B.");
    
    def test_LessEqual(sefl):
        a=5;
        b=5;
        sefl.assertLessEqual(a,b,"A debe ser menor o igual que B.");


    # @classmethod
    # def tearDownClass(cls):
    #     print('Final de la ejecución');
    #     print('Base de datos eliminada');
    #     print('Cerrando entorno.');
    #     print('Entorno cerrado');


    # def tearDown (self):
    #     print("Borrando dato...");
    #     print('Base de datos a valor inicial. ');
    #     print('Guardando resultado del caso. ');

if __name__ == "__main__":
    unittest.main();