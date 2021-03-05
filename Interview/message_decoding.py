"""How Many Ways to Decode This Message?"""

storage = {}
alphabet = ''

# Build the alphabet
for i in range(ord('a'), ord('z')+1):
    alphabet += chr(i)

# Dumb to storage the Unicode of the alphabet
for i in range(len(alphabet)):
    storage[str(i+1)] = alphabet[i]


def nuw_ways(num):
    """Show how many ways to Decode the message"""
    count = 0
    num = str(num)

    if num == '':                       # If data not invalid
        return 'Empty'
    if (len(num) > 2) | (num[0] in ['0', '-', ' ']):
        return 'Out of Length'
    elif len(num) == 1:                 # For data from 1-9
        count += 1
        print(num, ':', storage[num])
    elif len(num) == 2:                 # For data from 10-26
        for n in num:
            count += 1
            print(n, ':', storage[n])
        count += 1
        print(num, ':', storage[num])

    return count


data = '26'     # data = [1 - 26] | [a - z]
print('Total ways:', nuw_ways(data))
