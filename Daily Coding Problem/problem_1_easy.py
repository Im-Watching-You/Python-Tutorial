"""Daily Coding Problem: Problem #1 [Easy]"""

"""
    Description:
        Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
    Example:
        Given_list [10, 15, 3, 7] and k = 17, return true since 10 + 7 is 17.
"""


def add_up_to_k_v1(k, g_list, count=0):
    """With O(n^2) but more accurate"""
    for i in range(len(g_list) - 1):
        for n in range(i + 1, len(g_list)):
            if g_list[i] + g_list[n] == k:
                print("{0} + {1} = {2}".format(g_list[i], g_list[n], k))
                count += 1

    if count == 0:
        print("There are no numbers that return any two numbers from the list add up to k.")


def add_up_to_k_v2(k, g_list, count=0):
    """With O(n)"""
    for i, val in enumerate(g_list):
        if k - val in g_list[i + 1:]:
            print("{0} + {1} = {2}".format(val, g_list[g_list.index(k - val)], k))
            count += 1

    if count == 0:
        print("There are no numbers that return any two numbers from the list add up to k.")


def add_up_to_k_v3(k, g_list):
    """With O(n), which show True if two numbers from the list add up to k."""
    potential_solutions = set()
    for n in g_list:
        if n in potential_solutions:
            return True
        potential_solutions.add(k - n)

    return False


# Execution
equal = 17
given_list = [10, 14, 3, 7, 1, 16, 2, 15]
# add_up_to_k_v1(equal, given_list)
# add_up_to_k_v2(equal, given_list)
assert add_up_to_k_v3(equal, given_list)
