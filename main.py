import advance_operations as ad_calculator
import arithmetic_operations as calculator
import user_interface as ui


#Display welcome message

ui.display_message("Welcome to the Python Calculator!")

#Get user input

num1 = ui.get_number_input("Enter first number: ")
num2 = ui.get_number_input("Enter second number: ")


#choose operation
operation = ui.operation_selection()

#perform operations

if operation =='+':
   result = calculator.add(num1, num2)

elif operation =='-':
   result = calculator.sub(num1, num2)

elif operation =='*':
   result = calculator.multiply(num1, num2)


elif operation =='/':
   result = calculator.divide(num1, num2)


elif operation =='sqrt':
   result = ad_calculator.square_root(num1)

elif operation =='pow':
   result = ad_calculator.power(num1,num2)



#Display the result

ui.display_message(f'Result: {result}')