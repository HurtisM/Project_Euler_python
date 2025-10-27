# Problem 58
# Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.
#
# 37 36 35 34 33 32 31
# 38 17 16 15 14 13 30
# 39 18  5  4  3 12 29
# 40 19  6  1  2 11 28
# 41 20  7  8  9 10 27
# 42 21 22 23 24 25 26
# 43 44 45 46 47 48 49
#
# It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is
# that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 =~ 62%.
#
# If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed.
# If this process is continued, what is the side length of the square spiral for which the ratio of primes along
# both diagonals first falls below 10%?
import math

def is_prime(n):
    """Hybrid primality test: trial division for small numbers, Miller-Rabin for large."""
    if n < 2:
        return False
    if n in (2, 3, 5, 7, 11):
        return True
    if n % 2 == 0:
        return False

    if n < 10 ** 6:
        # trial division for small numbers
        for i in range(3, int(math.isqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True
    else:
        # deterministic Miller-Rabin for n < 2^32
        d = n - 1
        r = 0
        while d % 2 == 0:
            d //= 2
            r += 1
        for a in (2, 7, 61):
            if a >= n:
                continue
            x = pow(a, d, n)
            if x == 1 or x == n - 1:
                continue
            for _ in range(r - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    break
            else:
                return False
        return True


def sol():
    primes = 0
    n = 3
    while True:
        prime_in_layer = 0
        for i in range(4):
            roh = n**2 - i*(n-1)
            if is_prime(roh):
                prime_in_layer += 1
        primes += prime_in_layer

        # check ratio after first layer
        total_diagonals = 2*n - 1
        if n > 3 and (primes / total_diagonals) * 100 < 10:
            break
        n += 2  # spiral grows by 2 per layer
    return n


if __name__ == '__main__':
    print(sol())
