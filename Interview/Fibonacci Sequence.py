"""Fibonacci Sequence"""

# # Fibonacci
# a, b = 0, 1
# for _ in range(10):
#     print(a)
#     a, b = b, a + b


# Fibonacci generator
def fib(num):
    a, b = 0, 1
    for i in range(num):
        yield '{}: {}'.format(i+1, a)
        a, b = b, a + b


for item in fib(10):
    print(item)
