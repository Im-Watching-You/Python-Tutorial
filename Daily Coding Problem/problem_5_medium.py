"""Daily Coding Problem: Problem #5 [Medium]"""

"""
    Description:
        cons(a, b) constructs a pair, and car(pair) and cdr(pair)
        returns the first and last element of that pair.

    Example:
        car(cons(3, 4)) returns 3.
        cdr(cons(3, 4)) returns 4.
"""


def cons(a, b):
    """Сonstruct a pair"""
    return lambda f: f(a, b)


def car(f):
    """Return the first element of the pair"""
    z = lambda x, y: x
    return f(z)


def cdr(f):
    """Return the last element of the pair"""
    z = lambda x, y: y
    return f(z)


# Execution
assert car(cons(3, 4)) == 3
assert cdr(cons(3, 4)) == 4
