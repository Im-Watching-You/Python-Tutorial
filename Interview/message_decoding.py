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

    if num == '':
        return 'Empty'
    if (len(num) > 2) | (num[0] in ['0', '-', ' ']):
        return 'Out of Length'
    elif len(num) == 1:
        count += 1
        print(storage[num])
    elif len(num) == 2:
        for n in num:
            count += 1
            print(storage[n])
        count += 1
        print(storage[num])

    return count


data = '12'     # data = [1 - 26] | [a - z]

print(nuw_ways(data))
