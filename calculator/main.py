from calculator.arithmetic_operations import add, sub, multiply, divide
from calculator.advance_operations import square_root, power, factorial
from calculator.user_interface import display_message, get_number_input, operation_selection



def main():
   while True:

      #Display welcome message
      display_message("\nWelcome to the Python Calculator!")

      #Get user input one
      num1 = get_number_input("Enter first number: ")

      #choose operation
      operation = operation_selection()

      #Check if the user wants to exit
      if operation == 'q':
         display_message("Thank you for using the calculator. Goodbye!")
         break

      #perform basic operations
      if operation in ['+', '-', '*', '/']:
            
            #Get user input two
            num2 = get_number_input("Enter second number: ")

            #check if the user is trying to divide by zero
            if operation =='/' and num2 ==0:
                  display_message("Error division by zero")
                  continue

            if operation =='+':
                  result = add(num1, num2)

            elif operation =='-':
                  result = sub(num1, num2)

            elif operation =='*':
                  result = multiply(num1, num2)

            elif operation =='/':
                  result = divide(num1, num2)


      #perform advance operations
      elif operation in ['sqrt', 'pow', 'fact']:
            if operation =='sqrt':
                  result = square_root(num1)

            elif operation =='pow':
                  #Get user input two
                  num2 = get_number_input("Enter second number: ")
                  result = power(num1,num2)
            
            elif operation =='fact':
                  result = factorial(int(num1))

      #Display the result
      display_message(f'Result:  {result}')



if __name__ == "__main__":
    main()