import random


def common_elements():
    first_set = set([3 * i for i in range(1, random.randint(2, 100))])
    second_set = set([5 * i for i in range(1, random.randint(2, 100))])
    return first_set.intersection(second_set)


print(common_elements())
