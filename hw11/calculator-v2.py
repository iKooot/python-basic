first_number = None
second_number = None
do_operations = 'yes'

first_number_message = 'Please enter first number\n'
second_number_message = 'Please enter second number\n'
operation_message = 'Do you want to continue work with calculator? (yes | y)\n'
result_message = 'Your result is:'

while do_operations == 'y' or do_operations == 'yes':
    operator = input('Please enter action (Example +, -, *, /)\n')
    if operator == '+':
        first_number = int(input(first_number_message))
        second_number = int(input(second_number_message))
        print(result_message, first_number + second_number)
        do_operations = input(operation_message)

    elif operator == '-':
        first_number = int(input(first_number_message))
        second_number = int(input(second_number_message))
        print(result_message, first_number - second_number)
        do_operations = input(operation_message)

    elif operator == '*':
        first_number = int(input(first_number_message))
        second_number = int(input(second_number_message))
        print(result_message, first_number * second_number)
        do_operations = input(operation_message)

    elif operator == '/':
        first_number = int(input(first_number_message))
        second_number = int(input(second_number_message))

        if not second_number:
            print("You can't divides by 0")
            do_operations = input(operation_message)
        else:
            print(result_message, first_number / second_number)
            do_operations = input(operation_message)
    else:
        print('I dont recognise your operator')
        do_operations = input(operation_message)