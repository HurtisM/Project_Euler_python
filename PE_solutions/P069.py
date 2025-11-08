# Problem 69
# https://projecteuler.net/problem=69
from math import prod
from PE_utils import Primes


def best_n_upto(N):
    p = Primes(100)
    primes = p.primes_up_to(100)  # enough primes for moderate N
    n = 1
    best = 1
    for p in primes:
        if n * p > N:
            break
        n *= p
        best = n
    ratio = prod(p/(p-1) for p in primes[:primes.index(p)]) if best > 1 else 1
    return best, ratio


if __name__ == '__main__':
    limit = 1_000_000
    print(best_n_upto(limit))


# Suppose n is not the product of the first few primes (or repeats primes unnecessarily).
# Then either: n has larger primes → p / p-1 is closer to 1 → smaller ratio.
#
# n repeats primes → ratio is the same, because exponents don’t matter.
#
# Therefore, any number that cannot be written as the product of distinct small primes cannot beat the maximal ratio.
# n=30=2⋅3⋅5 → n/φ(n)=3.75
# n=60=2.2⋅3⋅5 → same primes → n/φ(n)=3.75
# n=42=2⋅3⋅7 → bigger primes → n/φ(n)=42/12=3.5<3.75
# So n=30 is better than 42, even though 42 is bigger, because it includes a larger prime (7)
