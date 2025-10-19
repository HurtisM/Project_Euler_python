# Problem 51
# By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values:
# 13, 23, 43, 53, 73, and 83, are all prime.
# By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example
# having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773,
# and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.
#
# Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit,
# is part of an eight prime value family.

from PE_utils import Primes
from itertools import combinations


def generate_masks(n):
    """Generate all non-empty masks (excluding last digit position)."""
    for r in range(1, n):  # mask sizes 1..n-1
        for combo in combinations(range(n - 1), r):  # skip last digit
            yield combo


def family_from_pattern(pattern):
    """Generate all numbers by replacing * with digits 0–9."""
    family = []
    for d in range(10):
        candidate = pattern.replace('*', str(d))
        # Skip leading zero cases
        if candidate[0] == '0':
            continue
        num = int(candidate)
        if p.is_prime(num):
            family.append(num)
    return family


def find_smallest_prime_in_family(target_family_size=8):
    prime = 11  # start from the smallest two-digit prime
    while True:
        if p.is_prime(prime):
            s = str(prime)
            n = len(s)
            for mask in generate_masks(n):
                # Build masked pattern
                pattern = ''.join('*' if i in mask else c for i, c in enumerate(s))

                # divisible by 3 trap
                fixed_sum = sum(int(c) for i, c in enumerate(s) if i not in mask)
                k = len(mask)
                # Count how many d would make divisible by 3
                dead_d = [d for d in range(10) if (fixed_sum + k * d) % 3 == 0]
                if 10 - len(dead_d) < target_family_size:
                    continue  # skip pattern

                # Generate and test the family
                family = family_from_pattern(pattern)
                if len(family) >= target_family_size:
                    print(f"Pattern: {pattern}")
                    print(f"Family of {len(family)} primes: {family}")
                    return min(family)
        prime += 2  # skip even numbers


if __name__ == "__main__":
    p = Primes(10000)
    result = find_smallest_prime_in_family(8)
    print(f"\nSmallest prime in an eight-prime family: {result}")
