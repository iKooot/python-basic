# example_list = [1, 3, 5]
# example_list = [6]
example_list = []

# result = 0
# for i, el in enumerate(example_list):
#     if not i % 2:
#         result += el
#         print(el)
#
# if len(example_list):
#     result *= example_list[-1]
#
# print(result)

result = 0

if len(example_list):
    result = sum([num for i, num in enumerate(example_list) if not i % 2]) * max(example_list)

print(result)