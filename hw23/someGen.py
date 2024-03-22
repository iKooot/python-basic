from inspect import isgenerator
from typing import Generator


def my_pow(x: int) -> int:
    return x ** 2


def some_gen(begin: int, end: int, func: callable) -> Generator[int, None, None]:
    count = 0
    while count < end:
        yield begin
        begin = func(begin)
        count += 1


gen = some_gen(2, 4, pow)

assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')
