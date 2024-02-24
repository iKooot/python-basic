user_number = int(input('Enter your number'))

number1, rest1 = divmod(user_number, 10000)
number2, rest2 = divmod(rest1, 1000)
number3, rest3 = divmod(rest2, 100)
number4, rest4 = divmod(rest3, 10)
number5, _ = divmod(rest4, 1)

result = str(number5) + str(number4) + str(number3) + str(number2) + str(number1)
print(result)