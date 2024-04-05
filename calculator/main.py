from calculator.arithmetic_operations import add, sub, multiply, divide
from calculator.advance_operations import square_root, power
from calculator.user_interface import display_message, get_number_input, operation_selection


#Display welcome message

display_message("Welcome to the Python Calculator!")

#Get user input

num1 = get_number_input("Enter first number: ")
num2 = get_number_input("Enter second number: ")


#choose operation
operation = operation_selection()

#perform operations

if operation =='+':
   result = add(num1, num2)

elif operation =='-':
   result = sub(num1, num2)

elif operation =='*':
   result = multiply(num1, num2)


elif operation =='/':
   result = divide(num1, num2)


elif operation =='sqrt':
   result = square_root(num1)

elif operation =='pow':
   result = power(num1,num2)



#Display the result

display_message(f'Result: {result}')