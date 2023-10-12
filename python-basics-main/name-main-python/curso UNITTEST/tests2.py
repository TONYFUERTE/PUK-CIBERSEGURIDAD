import unittest


class tests(unittest.TestCase):

    def test_Equal(self):
        self.assertEqual(1, 1, 'Deben ser iguales.');
    
    def test_resta(self):
        self.assertTrue(1-1== 0, 'La resta debe estar bien.');
    
    def test_sum(self):
        self.assertFalse (False, 'Sólo da error si la condición es True');

if __name__ == "__main__":
    unittest.main();