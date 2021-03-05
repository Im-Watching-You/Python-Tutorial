"""First recurring char in a string"""


def first_recurring(given_string):
    """Get the first recurring char in a string"""
    counts = {}
    for char in given_string:
        if char in counts:
            return char
        else:
            counts[char] = 1
    return None


# Execution
string = 'ECDBACE'
print(first_recurring(string))
