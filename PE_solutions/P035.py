# Problem 35
# The number, 197, is called a circular prime because all rotations of the digits:
# 197, 971 and 719, are themselves prime.
#
# There are thirteen such primes below 100: 2,3,5,7,11,13,17,31,37,71,73,79 and 97.
#
# How many circular primes are there below one million?
def primes_less_than(N):
    is_prime = [False, False] + [True]*(N-2)
    for num in range(2, int(N**0.5)+1):
        if is_prime[num]:
            for multiple in range(num*num, N, num):
                is_prime[multiple] = False
    return [i for i, p in enumerate(is_prime) if p]


def rotations(n):
    s = str(n)
    return {int(s[i:] + s[:i]) for i in range(len(s))}


def is_valid_candidate(n):
    if n < 10:
        return True
    return not any(d in '024568' for d in str(n))


def find_circular_primes(N):
    numbers = set(primes_less_than(N))
    circular_primes = set()

    for n in numbers:
        if n in circular_primes or not is_valid_candidate(n):
            continue
        rots = rotations(n)
        if rots.issubset(numbers):
            circular_primes.update(rots)

    return sorted(circular_primes)


if __name__ == "__main__":
    print(len(find_circular_primes(1000000)))
