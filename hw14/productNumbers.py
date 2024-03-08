user_input = input("Enter a number:\n")

result = None
do_calculation = True

while do_calculation:
    if result is None:
        temp_result = None
        for number in [int(number) for number in user_input]:
            if temp_result is None:
                temp_result = number
                continue
            temp_result *= number
        result = temp_result

    if result >= 10:
        temp_result = None
        for number in [int(digit) for digit in str(result)]:
            if temp_result is None:
                temp_result = number
                continue
            temp_result *= number
        result = temp_result
    else:
        print(result)
        do_calculation = False