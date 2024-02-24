import random

random_length = random.randint(3, 10)
random_numbers = [random.randint(1, 100) for _ in range(random_length)]

result = [random_numbers[1], random_numbers[2], random_numbers[-2]]

print(result)