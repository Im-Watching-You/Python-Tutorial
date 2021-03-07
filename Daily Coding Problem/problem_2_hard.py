"""Daily Coding Problem: Problem #2 [Hard]"""

from functools import reduce

"""
    Description:
        Given an array of integers, return a new array such that
        each element at index i of the new array is the product of
        all the numbers in the original array except the one at i.
    Example:
        input = [1, 2, 3, 4, 5]
        output = [120, 60, 40, 30, 24]
"""


def product_array_v1(old_list):
    """With Division"""
    new_list = []

    for i in old_list:
        new_val = int(reduce(lambda x, y: x * y, old_list) / i)
        new_list.append(new_val)

    return new_list


def product_array_v2(old_list):
    """Without Division"""
    new_list = []

    for i in range(len(old_list)):
        temp_list = old_list[:]
        del temp_list[i]

        new_val = reduce(lambda x, y: x * y, temp_list)
        new_list.append(new_val)

    return new_list


# Execution
given_list = [1, 2, 3, 4, 5]
print(product_array_v1(given_list))
print(product_array_v2(given_list))
