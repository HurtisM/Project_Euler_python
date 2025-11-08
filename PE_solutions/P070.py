# Problem 70
#
from sympy import primerange

LIMIT = 10_000_000


# Permutation check using digit counts
def are_permutations(a, b):
    if len(str(a)) != len(str(b)):
        return False
    count = [0]*10
    for d in str(a):
        count[int(d)] += 1
    for d in str(b):
        count[int(d)] -= 1
    return all(x == 0 for x in count)


def sol():
    # Generate all primes up to LIMIT // 2 (largest possible prime factor for n < LIMIT)
    primes = list(primerange(2, LIMIT // 2 + 1))

    best_n = 0
    best_ratio = float('inf')
    best_phi = 0

    # Iterate over semi primes
    for i, p in enumerate(primes):
        if p * p >= LIMIT:
            break  # p*q will exceed LIMIT
        for q in primes[i:]:
            n = p * q
            if n >= LIMIT:
                break
            phi_n = (p - 1) * (q - 1)
            ratio = n / phi_n
            if ratio < best_ratio and are_permutations(n, phi_n):
                best_ratio = ratio
                best_n = n
                best_phi = phi_n
    return best_n, best_phi


if __name__ == '__main__':
    number, phi = sol()
    print("Answer:")
    print("n =", number)
    print("φ(n) =", phi)
    print("n/φ(n) =", number / phi)
