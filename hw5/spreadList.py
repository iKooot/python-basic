import math
user_list = list(input('Enter data for list\n'))

# user_list = [1, 2, 3, 4, 5, 6]
# user_list = [1, 2, 3]
# user_list = [1, 2, 3, 4, 5]
# user_list = [1]
# user_list = []

first_list = []
second_list = []
result_list = []
middle = None

if len(user_list) % 2:
    middle = len(user_list) // 2 + 1
    first_list += user_list[:middle]
    second_list += user_list[middle:]
else:
    middle = len(user_list) // 2
    first_list += user_list[:middle]
    second_list += user_list[middle:]

result_list.append(first_list)
result_list.append(second_list)

print(result_list)