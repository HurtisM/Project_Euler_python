# Problem 41
# We shall say that an n-digit number is pandigital if it makes use of all the digits
#  1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
#
# What is the largest n-digit pandigital prime that exists?
import itertools


def pandigitals(num_digits):
    perm = list(itertools.permutations(range(1, num_digits+1), num_digits))
    numbers = [int(''.join(map(str, t))) for t in perm]
    filtered = [n for n in numbers if n % 10 not in (2, 4, 6, 8, 5, 0)]
    return sorted(filtered, reverse=True)


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def sol():
    for order in range(8, 0, -1):
        for i in pandigitals(order):
            if is_prime(i):
                return order, i
    return 0


if __name__ == "__main__":
    print(sol())
