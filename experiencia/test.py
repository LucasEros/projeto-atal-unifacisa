from unittest import TestCase, main
from solucao import melhor_experiencia
from time import time


class TestEncontroMarcado(TestCase):
    def setUp(self):
        self.C = [("Caviar", 100, 20), ("Pizza", 20, 5), ("Bode", 11, 10), ("Lagosta", 90, 15)]

    def test_caviar(self):
        self.assertListEqual(melhor_experiencia(100, self.C), ["Caviar"])

    def test_bode_lagosta(self):
        self.assertEqual(len(melhor_experiencia(110, self.C)), 2)
        self.assertIn("Bode", melhor_experiencia(110, self.C))
        self.assertIn("Lagosta", melhor_experiencia(110, self.C))

    def test_caviar_pizza(self):
        self.assertEqual(len(melhor_experiencia(120, self.C)), 2)
        self.assertIn("Caviar", melhor_experiencia(120, self.C))
        self.assertIn("Pizza", melhor_experiencia(120, self.C))


if __name__ == "__main__":
    main()
