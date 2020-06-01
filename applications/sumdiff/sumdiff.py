"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

# q = set(range(1, 10))
# q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6


def sum_and_diff(numbers):
    my_dict = {"f(0)+f(0)": numbers[0] + numbers[0]}
    for i in range(1, len(numbers)):
        sum_1 = numbers[i] + numbers[i]
        sum_2 = numbers[i] + numbers[i-1]