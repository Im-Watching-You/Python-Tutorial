"""Fibonacci Sequence"""

from functools import lru_cache


class Fibonacci:
    """Fibonacci Sequence"""

    def __init__(self, num):
        """param num: int, number of Fibonacci sequences"""
        self.num = num

    def fib_1(self):
        """Version 1: Short Fibonacci"""
        a, b = 1, 1
        for i in range(self.num):
            print(i + 1, ':', a)
            a, b = b, a + b

    def fib_2(self):
        """Version 2: Fibonacci Generator"""

        def fibonacci(n):
            """Calculate the Fibonacci Sequence with yield"""
            a, b = 1, 1
            for i in range(n):
                yield '{} : {}'.format(i + 1, a)
                a, b = b, a + b

        # Execution
        for item in fibonacci(self.num):
            print(item)

    def fib_3(self):
        """Version 3: Fibonacci with fibonacci_cache dictionary memorization"""
        fibonacci_cache = {}

        def fibonacci(n):
            """Calculate the Fibonacci Sequence with cache dictionary"""
            value = 0

            if n in fibonacci_cache:
                return fibonacci_cache[n]

            if n == 1:
                value = 1
            elif n == 2:
                value = 1
            elif n > 2:
                value = fibonacci(n - 1) + fibonacci(n - 2)

            fibonacci_cache[n] = value
            return value

        # Execution
        for i in range(self.num):
            print(i + 1, ':', fibonacci(i + 1))

    def fib_4(self):
        """Version 4: Fibonacci with lru_cache memorization"""

        @lru_cache(maxsize=1000)
        def fibonacci(n):
            """Calculate the Fibonacci Sequence with lru_cache"""

            if n == 1:
                return 1
            elif n == 2:
                return 1
            elif n > 2:
                return fibonacci(n - 1) + fibonacci(n - 2)

        # Execution
        for i in range(self.num):
            print(i + 1, ':', fibonacci(i + 1))


number = 1000
fibonacci = Fibonacci(number)
fibonacci.fib_1()
# fibonacci.fib_2()
# fibonacci.fib_3()
# fibonacci.fib_4()
