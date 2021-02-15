"""Generator of a_z, A_Z"""

import random
import string


def gener_A_Z_V1(given_num, text=''):
    """Version 1 with random.choice(string.ascii_letters)"""
    for i in range(given_num):
        if i % 2 == 0:
            text += random.choice(string.ascii_letters[:26])
        else:
            text += random.choice(string.ascii_letters[26:])
    print(text)


def gener_A_Z_V2(given_num, text=''):
    """Version 2 with chr(random.randint(ord('a'), ord('z')))"""
    for i in range(given_num):
        if i % 2 == 0:
            text += chr(random.randint(ord('a'), ord('z')))
        else:
            text += chr(random.randint(ord('A'), ord('Z')))
    print(text)


# Execution
num_letters = 10
gener_A_Z_V1(num_letters)
