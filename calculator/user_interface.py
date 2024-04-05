def display_message(message):
    print(message)


def display_error(message):
    print('Error: ' + message)


def get_number_input(prompt):
    while True:
        try:
            return float(input(prompt))

        except ValueError:
            display_error("Invalid input. Please enter a number.")


def operation_selection():
    while True:
        operation = input("Choose an operation (+, -, *, /, sqrt, pow, fact,'reset' or 'q' to quit): ")
        try:
            if operation in ['+', '-', '*', '/', 'sqrt', 'pow', 'fact','reset', 'q']:
                return operation
            
            else:
               display_error("Invalid input. Please enter a valid operation.")

        except ValueError:
            display_error("Invalid input. Please enter a valid operation.")
