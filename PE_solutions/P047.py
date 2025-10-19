# Problem 47
# The first two consecutive numbers to have two distinct prime factors are:
#               14 = 2 x 7
#               15 = 3 x 5
# The first three consecutive numbers to have three distinct prime factors are:
#               644 = 2^2 x 7 x 23
#               645 = 3 x 5 x 43
#               646 = 2 x 17 x 19
# Find the first four consecutive integers to have four distinct prime factors each.
# What is the first of these numbers?
from PE_utils import MathUtils


def find_consecutive_integers():
    consecutive_count = 0
    current_integer = 1

    while consecutive_count < 4:
        if (
            MathUtils.prime_factors_count(current_integer) == 4
            and MathUtils.prime_factors_count(current_integer + 1) == 4
            and MathUtils.prime_factors_count(current_integer + 2) == 4
            and MathUtils.prime_factors_count(current_integer + 3) == 4
        ):
            return current_integer
        else:
            current_integer += 1
    return current_integer

result = find_consecutive_integers()
print("The first of the four consecutive integers:", result)