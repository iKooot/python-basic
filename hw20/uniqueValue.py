def find_unique_value(some_list: list) -> int:
    values = {}

    for value in some_list:
        if value not in values:
            values[value] = 1
        else:
            values[value] += 1

    for key, value in values.items():
        if value == 1:
            return key


assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")