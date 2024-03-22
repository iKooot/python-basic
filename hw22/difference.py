from __future__ import annotations


def min_max_gen(numbers: tuple[int | float, ...]) -> tuple[int | float, int | float]:
    yield min(numbers), max(numbers)


def difference(*args: int | float) -> int | float:
    if not args:
        return 0
    min_number, max_number = next(min_max_gen(args))
    return round(max_number - min_number, 2)


assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')
