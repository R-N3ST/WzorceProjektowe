import unittest
from unittest.mock import patch

from coffee_machine import (
    EspressoMachineFactory,
    LatteMachineFactory,
    CappuccinoMachineFactory,
    MochaMachineFactory,
)


class CoffeeMachineTests(unittest.TestCase):
    def test_create_espresso(self):
        espresso_factory = EspressoMachineFactory()
        espresso = espresso_factory.create_coffee()
        self.assertIsInstance(espresso, Espresso)

    def test_create_latte(self):
        latte_factory = LatteMachineFactory()
        latte = latte_factory.create_coffee()
        self.assertIsInstance(latte, Latte)

    def test_create_cappuccino(self):
        cappuccino_factory = CappuccinoMachineFactory()
        cappuccino = cappuccino_factory.create_coffee()
        self.assertIsInstance(cappuccino, Cappuccino)

    def test_create_mocha(self):
        mocha_factory = MochaMachineFactory()
        mocha = mocha_factory.create_coffee()
        self.assertIsInstance(mocha, Mocha)


if __name__ == "__main__":
    unittest.main()