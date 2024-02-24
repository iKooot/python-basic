# example_list = [0, 1, 0, 12, 3]
# example_list = [0]
# example_list = [1, 0, 13, 0, 0, 0, 5]
example_list = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

# first variant
# first_list = []
# second_list = []
#
# for el in example_list:
#     if not el == 0:
#         first_list.append(el)
#         continue
#     second_list.append(el)
#
# print(first_list + second_list)

# second variant
non_zero_elements = [el for el in example_list if el != 0]
zero_elements = [el for el in example_list if el == 0]

result_list = non_zero_elements + zero_elements

print(result_list)