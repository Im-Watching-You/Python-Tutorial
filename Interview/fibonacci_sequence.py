"""Fibonacci Sequence"""

# # Fibonacci
# a, b = 0, 1
# for _ in range(10):
#     print(a)
#     a, b = b, a + b


def fib(num):
    """Fibonacci generator"""
    a, b = 0, 1
    for i in range(num):
        yield '{}: {}'.format(i+1, a)
        a, b = b, a + b


# Execution
for item in fib(10):
    print(item)
