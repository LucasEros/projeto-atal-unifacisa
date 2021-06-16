from unittest import TestCase, main
from solucao import minimo_operacoes
from time import time


class TestMinimoOperacoes(TestCase):
    def setUp(self):
        self.D1 = "CCCVCVVC"
        self.D2 = "VVVVV"
        self.D3 = "CVCVC"

    def test_previamente_correto(self):
        inicio = time()
        self.assertEqual(minimo_operacoes(self.D2, 4), 0)
        fim = time()
        self.assertLessEqual(fim-inicio, 0.2)

    def test_algumas_operacoes(self):
        inicio = time()
        self.assertEqual(minimo_operacoes(self.D1, 3), 3)
        fim = time()
        self.assertLessEqual(fim-inicio, 0.2)

    def test_impossivel(self):
        inicio = time()
        self.assertEqual(minimo_operacoes(self.D3, 4), -1)
        fim = time()
        self.assertLessEqual(fim-inicio, 0.2)


if __name__ == "__main__":
    main()
