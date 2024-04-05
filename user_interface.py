def display_message(message):
    print(message)



def get_number_input(prompt):
    while True:
        try:
            return float(input(prompt))

        except ValueError:
            print("Invalid input. Please enter a number.")


def operation_selection():
    while True:
        operation = input("Choose an operation (+, -, *, /, sqrt, pow): ")
        try:
            if operation in ['+', '-', '*', '/', 'sqrt', 'pow']:
                return operation
            

        except ValueError:
            print("Invalid input. Please enter a valid operation.")
