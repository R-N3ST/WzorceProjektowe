# Ernest Kozikowski 14017 - wzroce projektowe
class Coffee:
    def brew(self):
        pass

class Espresso(Coffee):
    def brew(self):
        print("Brewing Espresso...")

class Latte(Coffee):
    def brew(self):
        print("Brewing Latte...")

class Cappuccino(Coffee):
    def brew(self):
        print("Brewing Cappuccino...")

class Mocha(Coffee):
    def brew(self):
        print("Brewing Mocha...")

class CoffeeMachineFactory:
    def create_coffee(self):
        pass

    def add_milk(self):
        pass

    def choose_grind_thickness(self):
        pass

    def choose_brew_temperature(self):
        pass

class EspressoMachineFactory(CoffeeMachineFactory):
    def create_coffee(self):
        return Espresso()

    def add_milk(self):
        print("Adding milk to the coffee...")

    def choose_grind_thickness(self):
        print("Choosing grind thickness for Espresso...")

    def choose_brew_temperature(self):
        print("Choosing brew temperature for Espresso...")

class LatteMachineFactory(CoffeeMachineFactory):
    def create_coffee(self):
        return Latte()

    def add_milk(self):
        print("Adding milk to the coffee...")

    def choose_grind_thickness(self):
        print("Choosing grind thickness for Latte...")

    def choose_brew_temperature(self):
        print("Choosing brew temperature for Latte...")

class CappuccinoMachineFactory(CoffeeMachineFactory):
    def create_coffee(self):
        return Cappuccino()

    def add_milk(self):
        print("Adding milk to the coffee...")

    def choose_grind_thickness(self):
        print("Choosing grind thickness for Cappuccino...")

    def choose_brew_temperature(self):
        print("Choosing brew temperature for Cappuccino...")

class MochaMachineFactory(CoffeeMachineFactory):
    def create_coffee(self):
        return Mocha()

    def add_milk(self):
        print("Adding milk to the coffee...")

    def choose_grind_thickness(self):
        print("Choosing grind thickness for Mocha...")

    def choose_brew_temperature(self):
        print("Choosing brew temperature for Mocha...")

def get_user_input():
    print("Select the type of coffee: (In words - not numerically)")
    print("1. Espresso")
    print("2. Latte")
    print("3. Cappuccino")
    print("4. Mocha")
    choice = input("Enter your choice: ")
    return choice

def control_sugar(coffee):
    sugar_amount = input("Enter the desired sugar amount (in teaspoons): ")
    print(f"Adding {sugar_amount} teaspoons of sugar to the coffee...")
    return sugar_amount

def main():
    choice = get_user_input()

    factories = {
        'Espresso': EspressoMachineFactory(),
        'Latte': LatteMachineFactory(),
        'Cappuccino': CappuccinoMachineFactory(),
        'Mocha': MochaMachineFactory()
    }

    if choice in factories:
        factory = factories[choice]
        coffee = factory.create_coffee()
        coffee.brew()
        factory.add_milk()
        factory.choose_grind_thickness()
        factory.choose_brew_temperature()
        sugar_amount = control_sugar(coffee)

        print(f"You have made a {choice} with {sugar_amount} teaspoons of sugar.")
    else:
        print("Invalid choice! Please try again with different data <3")

if __name__ == '__main__':
    main()