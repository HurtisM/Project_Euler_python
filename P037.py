# Problem 37
# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits
# from left to right, and remain prime at each stage:3797, 797, 97, and 7.
# Similarly, we can work from right to left: 379,37, 7.
#
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
#
# NOTE:2, 3, 5, and 7 are not considered to be truncatable primes.

def primes_less_than(N):
    is_prime = [False, False] + [True]*(N-2)
    for num in range(2, int(N**0.5)+1):
        if is_prime[num]:
            for multiple in range(num*num, N, num):
                is_prime[multiple] = False
    return [i for i, p in enumerate(is_prime) if p]


def truncated(n):
    s = str(n)
    left = {int(s[i:]) for i in range(len(s))}
    right = {int(s[:-i]) for i in range(1, len(s)) if s[:-i]}
    return left | right


def find_truncatable_primes(N):
    numbers = set(primes_less_than(N))
    truncatable_primes = []

    for n in numbers:
        trunc = truncated(n)
        if trunc.issubset(numbers) and n > 10:
            truncatable_primes.append(n)

    return sorted(truncatable_primes)


if __name__ == "__main__":
    print(sum(find_truncatable_primes(1000000)))
