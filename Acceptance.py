import unittest
from io import StringIO
from unittest.mock import patch

from coffee_machine import main


class CoffeeMachineAcceptanceTests(unittest.TestCase):
    def test_main_with_valid_choice(self):
        user_input = "2\n"
        expected_output = (
            "Select the type of coffee: (In words - not numerically)\n"
            "1. Espresso\n"
            "2. Latte\n"
            "3. Cappuccino\n"
            "4. Mocha\n"
            "Enter your choice: \n"
            "Brewing Latte...\n"
            "Adding milk to the coffee...\n"
            "Choosing grind thickness for Latte...\n"
            "Enter the desired beans thickness(in percentages): \n"
            "Choosing the [bean_thickness] bean thickness for our coffee...\n"
            "Choosing brew temperature for Latte...\n"
            "Enter the desired sugar amount (in teaspoons): \n"
            "Adding [sugar_amount] teaspoons of sugar to the coffee...\n"
            "You have made a Latte with [sugar_amount] teaspoons of sugar.\n"
        )

        with patch("sys.stdout", new=StringIO()) as fake_output:
            with patch("builtins.input", side_effect=user_input):
                main()

        self.assertEqual(fake_output.getvalue().strip(), expected_output)


if __name__ == "__main__":
    unittest.main()