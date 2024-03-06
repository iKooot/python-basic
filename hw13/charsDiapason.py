import string
diapason = input('Enter diapason (Ex. a-b)\n')
# diapason = 'a-c'
# diapason = 'a-a'
# diapason = 's-H'
# diapason = 'a-A'
first_char = diapason[0]
last_char = diapason[-1]

chars = f"{string.ascii_lowercase}{string.ascii_uppercase}"
start_index = chars.find(first_char)
end_index = chars.find(last_char) + 1
result = chars[start_index:end_index]

print(result)