import string
import keyword

variable_name = input("Enter variable name?\n")
is_valid = None

if variable_name[0].isdigit():
    is_valid = False
elif variable_name.isdigit():
    is_valid = False
elif keyword.iskeyword(variable_name):
    is_valid = False
elif any(char.isupper() or char.isspace() or (char in string.punctuation and char != '_') for char in variable_name):
    is_valid = False
else:
    is_valid = True

print(is_valid)