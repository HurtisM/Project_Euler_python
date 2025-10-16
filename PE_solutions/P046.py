# Problem 46
# It was proposed by Christian Goldbach that every odd composite number can be written
# as the sum of a prime and twice a square.
# 9=7+2x1^2
# 15 = 7 + 2 x 2^2
# 21 = 3 + 2 x 3^2
#
# It turns out that the conjecture was false.
# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
import timeit
import math


def primes(limit):                    #generate list of primes less than limit
    result = []
    sieve = [True for i in range(limit + 1)]
    for b in range(4, limit + 1, 2):
        sieve[b] = False
    a = 3
    while a ** 2 <= limit:
        if sieve[a]:
            for b in range(a ** 2, limit + 1, a):
                sieve[b] = False
        a += 2
    for a in range(2, limit + 1):
        if sieve[a]:
            result.append(a)
    return result


def sol(limit=10000):
    primes_list = primes(limit)
    primes_set = set(primes_list)

    for n in range(3, limit, 2):  # odd numbers only
        if n not in primes_set:  # only composite numbers
            works = False
            for p in primes_list:
                if p >= n:
                    break
                remainder = n - p
                if remainder % 2 == 0:
                    sq = int(math.isqrt(remainder // 2))
                    if 2 * sq * sq == remainder:
                        works = True
                        break
            if not works:
                return n  # this is the first odd composite that fails
    return None

# faster method , precompute the double squares 2,8,18,32,... up to (limit // 2 ) +1
# then just check if any number (odd composite) - double square is not in primes
def goldbach_fast(limit=100000):
    primes_list = primes(limit)
    primes_set = set(primes_list)
    double_squares = [2 * i * i for i in range(1, int(math.sqrt(limit // 2)) + 1)]

    for n in range(3, limit, 2):
        if n not in primes_set:  # odd composite
            if not any((n - ds) in primes_set for ds in double_squares if ds < n):
                return n


if __name__ == "__main__":
    time_my_sol = timeit.timeit(lambda: sol(), number=100)
    time_goldbach_fast = timeit.timeit(lambda: goldbach_fast(), number=100)

    print(f"my solution  time: {time_my_sol:.6f} seconds")
    print(f"using goldbach_fast solution time: {time_goldbach_fast:.6f} seconds")

    print(sol())
