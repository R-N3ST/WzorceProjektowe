import unittest
from io import StringIO
from unittest.mock import patch

from coffee_machine import Espresso, Latte, Cappuccino, Mocha


class CoffeeTests(unittest.TestCase):
    def test_espresso_brew(self):
        espresso = Espresso()
        with patch("sys.stdout", new=StringIO()) as fake_output:
            espresso.brew()
            self.assertEqual(fake_output.getvalue().strip(), "Brewing Espresso...")

    def test_latte_brew(self):
        latte = Latte()
        with patch("sys.stdout", new=StringIO()) as fake_output:
            latte.brew()
            self.assertEqual(fake_output.getvalue().strip(), "Brewing Latte...")

    def test_cappuccino_brew(self):
        cappuccino = Cappuccino()
        with patch("sys.stdout", new=StringIO()) as fake_output:
            cappuccino.brew()
            self.assertEqual(fake_output.getvalue().strip(), "Brewing Cappuccino...")

    def test_mocha_brew(self):
        mocha = Mocha()
        with patch("sys.stdout", new=StringIO()) as fake_output:
            mocha.brew()
            self.assertEqual(fake_output.getvalue().strip(), "Brewing Mocha...")


if __name__ == "__main__":
    unittest.main()