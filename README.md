### Ernest Kozikowski 14017

# Shared project for Design Patterns - Pana Prof. Marcina Albiniaka and for Advanced Programming - Pana Prof. Piotra Bobińkiego

Fullfill the related project with automatic testes: 
a. Unit   b. Integration c. Acceptance - 1 test per type

Base design - design pattern in python written in Visual Studio Code (Coffee Machine)



# DOCUMENTATION System structure:


# Class Definitions:

Coffee: Base class for different types of coffee.
Espresso, Latte, Cappuccino, Mocha: Subclasses of Coffee representing specific types of coffee.
CoffeeMachineFactory: Base class for coffee machine factories.
EspressoMachineFactory, LatteMachineFactory, CappuccinoMachineFactory, MochaMachineFactory: Subclasses of CoffeeMachineFactory representing different types of coffee machine factories.


# Helper Functions:
get_user_input(): Prompts the user to select a type of coffee and returns the choice.
grind_thickness(coffee): Prompts the user to enter the desired bean thickness and returns the input value.
control_sugar(coffee): Prompts the user to enter the desired sugar amount and returns the input value.


# The main() function:
Uses an infinite loop to continuously execute the coffee-making process until a valid choice is made.
Calls get_user_input() to get the user's choice of coffee.
Creates a dictionary factories that maps coffee names to their respective machine factories.
If the user's choice is valid (found in factories), it proceeds with the coffee-making process:
Retrieves the appropriate factory based on the user's choice.
Creates a coffee object using the factory's create_coffee() method.
Calls brew() on the coffee object to simulate brewing.
Calls various methods on the factory object to simulate adding milk, choosing grind thickness, and choosing brew temperature.
Calls grind_thickness() and control_sugar() to get additional user input.
Prints the type of coffee and sugar amount.
Breaks the loop to exit the program.
If the user's choice is invalid, it prints an error message and restarts the loop.


# Execution Entry Point:
if __name__ == '__main__': checks if the script is being run directly.
If true, it calls the main() function to start the coffee-making process.

# Test Scenario:

Test Case1: Ensure that the User can go through all the programm parts.

Test Case2: Ensure that the User got error pop-up when the input values are not meet to the commants creatiria.

Test Case3: Ensure that the 'brew' method can take Espresso, Latte, Mocha, Cappucino as arguments

Test Case4: Ensure that the sugar adding works as intended.

Test Case5: Ensure that the User can choose the brewing temperature.

# Issue found: The user cannot choose the brewing temperature
Aforementioned issue we can report in the tracking tool like Jira:

Environment: Visual Studio Code / Build: Not-known

Input Data:
Espresso, Latte, Cappucino, Mocha 

Reproduction steps:
1. Start the application
2. Fill the console with any of the related types of coffe(like 'Latte'
3. Type number between 0-10 in the sugar_amount terminal 
4. Proceed to the terminal information
5. Observe lack of brewing temperature option

Observed result:
The Coffee Machine programm does not contain 'brewing_temperature' picking option.

Expected result: 
The Coffee Machine temperature function works properly for all related cofee types.

Attachment: Screenshot or Video

### We can fix this issue by adding input function that will add the value to the brewing bar process.

# Used tools and libraries: 
unittest - It is a testing framework that is part of the Python standard library. It provides a set of tools and assertions for writing and running tests.

unittest.mock - It is a module within the unittest framework that provides mocking capabilities. It allows you to replace objects and control their behavior during tests, making it easier to isolate components and simulate certain conditions.

patch - It is a function from the unittest.mock module that is used as a decorator or a context manager to temporarily replace objects during tests. It is particularly useful for replacing standard output (sys.stdout) to capture and assert against printed output.

StringIO - It is a class from the io module that provides a file-like interface for working with strings as if they were files. It is used in combination with patch to capture the printed output from the code under test and compare it against expected output.
