# Problem 43
# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of
# each of the digits 0 to 9 in some order, but it also has a rather
# interesting sub-string divisibility property.
#
# Let d1 be the 1st digit,d2 be the 2nd digit, and so on. In this way, we note the following:
#
# d2d3d4 is divisible by 2
# d3d4d5 is divisible by 3
# d4d5d6 is divisible by 5
# d5d6d7 is divisible by 7
# d6d7d8 is divisible by 11
# d7d8d9 is divisible by 13
# d8d9d10 is divisible by 17
# Find the sum of all 0 to 9 pandigital numbers with this property.
import itertools


def pandigitals(num_digits):
    perm = list(itertools.permutations(range(0, num_digits), num_digits))
    numbers = [int(''.join(map(str, t))) for t in perm]
    return numbers


pandigitals = pandigitals(10)

valid = []
for number in pandigitals:
    s = str(number)
    if len(s) == 10:
        triplets = [int(s[i:i + 3]) for i in range(1, len(s) - 2)]
        if triplets[0] % 2 != 0:
            continue
        if triplets[1] % 3 != 0:
            continue
        if triplets[2] % 5 != 0:
            continue
        if triplets[3] % 7 != 0:
            continue
        if triplets[4] % 11 != 0:
            continue
        if triplets[5] % 13 != 0:
            continue
        if triplets[6] % 17 != 0:
            continue
        valid.append(number)

print(sum(valid))
