from functools import reduce


def fatorial(num: int) -> int:
    return 1 if num in (0, 1) else reduce(lambda x, y: x * y, range(1, num + 1))
