# Problem 33
# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to
# simplify it may incorrectly believe that 49/98=4/8, which is correct,
# is obtained by cancelling the 9s.
# We shall consider fractions like, 30/50=3/5, to be trivial examples.
# There are exactly four non-trivial examples of this type of fraction, less than one in value,
# and containing two digits in the numerator and denominator.
#
# If the product of these four fractions is given in its lowest common terms,
# find the value of the denominator.

from math import gcd


def sol():
    num_prod = 1
    den_prod = 1
    for i in range(12, 99):
        for j in range(i % 10*10, i % 10*10+10):
            a = i//10
            b = j % 10
            if 0 < b != a and i/j == a/b:
                num_prod *= i
                den_prod *= j
    common_divisor = gcd(num_prod, den_prod)
    return den_prod//common_divisor


if __name__ == "__main__":
    print(sol())
