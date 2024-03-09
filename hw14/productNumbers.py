user_input = input("Enter a number:\n")
# user_input = '999' # -> 2
# user_input = '1000' # -> 0
# user_input = '423' # -> 8
# user_input = '33' # -> 9
# user_input = '25' # -> 0
# user_input = '1' # -> 1
# user_input = '854' # -> 0

result = None
do_calculation = True

while do_calculation:
    temp_result = None
    for number in [int(number) for number in result or user_input]:
        if temp_result is None:
            temp_result = number
            continue
        temp_result *= number
    result = str(temp_result)

    if len(result) == 1:
        print(result)
        do_calculation = False