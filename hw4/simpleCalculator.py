operator = input('Please enter action (Example +, -, *, /)\n')

first_number = None
second_number = None
first_number_message = 'Please enter first number\n'
second_number_message = 'Please enter second number\n'
result_message = 'Your result is'

if operator == '+':
    first_number = int(input(first_number_message))
    second_number = int(input(second_number_message))
    print(result_message, first_number + second_number)

elif operator == '-':
    first_number = int(input(first_number_message))
    second_number = int(input(second_number_message))
    print(result_message, first_number - second_number)

elif operator == '*':
    first_number = int(input(first_number_message))
    second_number = int(input(second_number_message))
    print(result_message, first_number * second_number)

elif operator == '/':
    first_number = int(input(first_number_message))
    second_number = int(input(second_number_message))

    if not second_number:
        print("You can't divides by 0")
    else:
        print(result_message, first_number / second_number)
else:
    print('I dont recognise your operator')