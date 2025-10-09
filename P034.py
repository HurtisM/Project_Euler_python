# Problem 34
# 145 is a curious number, as 1!+4!+5!=1+24+120=145.
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#
# Note: As 1! and 2! are not sums they are not included.
import math


# just brute force approach.. still fast enough :-)
def sol():
    result = 0
    for number in range(3, 99999):
        if sum(math.factorial(int(c)) for c in str(number)) == number:
            result += number
    return result


if __name__ == "__main__":
    print(sol())
