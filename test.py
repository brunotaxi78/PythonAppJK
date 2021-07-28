import unittest
import calculadora

class TestCalculadora(unittest.TestCase):
    def teste_adiciona_int(self):
        res = calculadora.add(2,2)
        self.assertEqual(res,4)
    def teste_adiciona_dec(self):
        res = calculadora.add(5.3,2)
        self.assertEqual(res,7.3)
    def teste_adiciona_string_int(self):
        res = calculadora.add('bruno',2)
        self.assertEqual(res,'bruno2')
    def teste_adiciona_string_dec(self):
        res = calculadora.add('bruno',2.2)
        self.assertEqual(res,'bruno2.2')
    def teste_adiciona_string(self):
        res = calculadora.add('bruno','monteiro')
        self.assertEqual(res,'bruno monteiro')

if __name__ == "__main__":
    unittest.main()