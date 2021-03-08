"""Daily Coding Problem: Problem #4 [Hard]"""

"""
    Description:
        Given an array of integers, find the first missing positive integer in linear time and constant space.
        In other words, find the lowest positive integer that does not exist in the array.
        The array can contain duplicates and negative numbers as well.
    Example:
        The input [3, 4, -1, 1] should give 2.
        The input [1, 2, 0] should give 3.
        You can modify the input array in-place.
"""


def get_lost_value(g_list):
    # If the list is 'empty' or it has '0' or less values: return '1'
    if (g_list == []) or (max(g_list) <= 0):
        return 1

    # Remove '<= 0' values by filter and sort the list and remove the duplicates by set()
    g_set = set(filter(lambda n: n > 0, g_list))

    # Return lost value
    for i, val in enumerate(g_set, start=1):
        if i != val:
            return i

    return max(g_set) + 1


# Execution
given_list = [3, 2, -1, 1, 6, -3]
print(get_lost_value(given_list))

assert get_lost_value([3, 4, -1, 1]) == 2
assert get_lost_value([1, 2, 0]) == 3
assert get_lost_value([1, 2, 5]) == 3
assert get_lost_value([1]) == 2
assert get_lost_value([-1, -2]) == 1
assert get_lost_value([]) == 1
