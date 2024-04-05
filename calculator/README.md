# Python Claculator 

## Create Modules:

1) arithmetic_operations.py: 
This module will contain functions for basic arithmetic operations such as addition, subtraction, multiplication, and division.


2) advanced_operations.py: 
This module will contain functions for advanced arithmetic operations such as calculating square roots and powers.


3) user_interface.py: 
This module will contain functions for handling user input and output, such as displaying messages and getting input from the user.

## Use the Modules in Main Program

4) main.py:
When you run main.py, it will import the arithmetic_operations, advanced_operations, and user_interface modules, and use their functions to perform calculations and interact with the user


### Create Package Structure:
further by creating a package to organize our modules. We'll structure our project into a package named calculator with sub-packages for different functionalities.

calculator/
├── __init__.py
├── arithmetic_operations.py
├── advanced_operations.py
├── user_interface.py
└── main.py

from arithmetic_operations import add, subtract, multiply, divide
from advanced_operations import square_root, power
from user_interface import display_message, get_number_input, get_operation_choice

we've organized our modules into a package named calculator. Each module represents a specific aspect of the calculator program, such as arithmetic operations, advanced operations, and user interface handling. This package structure improves the organization and readability of the codebase, making it easier to manage and maintain as the project grows.

