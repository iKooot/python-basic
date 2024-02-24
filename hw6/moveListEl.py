# example_list = [12, 3, 4, 10]
# example_list = [1]
# example_list = []
example_list = [12, 3, 4, 10, 8]

if len(example_list):
    first_el = example_list[0]
    last_el = example_list[-1]

    example_list[0] = last_el
    example_list[-1] = first_el

print(example_list)