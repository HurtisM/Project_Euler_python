#Problem 24
#A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of
#the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically,
# we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
# 012   021   102   120   201   210
#What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

from math import factorial


def lexicographic_permutations(digits, seek):
    n = len(digits) - 1                                 # all permutation of number of n digits are n!
    seek_index = seek - 1                                # indexes are counting from 0 we are loking for number on nth place (seek) so index is seek-1
    wanted_number = ''
    if seek > factorial(n+1):                           # if idex of permutation in variable seek is higher than all permutations
        return "permutation out of range!"              # return error message
    while n >= 0:
        index = (seek_index // factorial(n))            # dividing seeking index by n!  for example looking for index 999999 // 9! = 2
        wanted_number += ''.join(digits[index])         # digit of number we are looking for is on index in string "digits"
        digits = digits[:index] + digits[index+1:]      # remove digit on index from available digits
        seek_index -= index * factorial(n)              #  999999 = 2*9!  + 274239
        n -= 1                                          # continue dividng by n! until n=0 (0 including)
    return wanted_number


if __name__ == "__main__":
    print(lexicographic_permutations("0123456789", 1000000))