user_number = int(input('Enter your number'))

number1, rest1 = divmod(user_number, 1000)
number2, rest2 = divmod(rest1, 100)
number3, rest3 = divmod(rest2, 10)
number4, _ = divmod(rest3, 1)

print(number1)
print(number2)
print(number3)
print(number4)