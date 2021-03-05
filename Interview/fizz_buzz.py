"""Fizz Buzz"""


def fizz_buzz(number):
    """Fizz Buzz checker"""
    if (number % 3 == 0) and (number % 5 == 0):
        print('Fizz Buzz')
    elif number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
        print('Buzz')
    else:
        print(number)


# Execution
for num in range(16):
    fizz_buzz(num)
