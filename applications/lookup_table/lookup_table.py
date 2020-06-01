import random
import math


def slow_fun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v


cache = {3: 5}


def slow_fun(x, y):
    """
    Rewrite slow_fun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    v = math.pow(x, y)

    if int(v) in cache:
        v = cache[int(v)]
    else:
        cache[int(v)] = math.factorial(v)
        v = cache[int(v)]

    v //= (x + y)
    v %= 982451653

    return v


# Do not modify below this line!


for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slow_fun(x, y)}')
