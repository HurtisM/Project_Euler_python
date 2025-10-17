# Problem 50
# The prime 41, can be written as the sum of six consecutive primes:
#               41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
#
# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
#
# Which prime, below one-million, can be written as the sum of the most consecutive primes?
from PE_utils import Primes


def sol(primes, limit):
    prime_set = set(primes)
    cumsum = [0]
    for prime in primes:
        cumsum.append(cumsum[-1] + prime)

    max_consecutive_primes = 0
    result_prime = 0

    for i in range(len(primes)):
        for j in range(i+max_consecutive_primes, len(primes)):
            current_sum = cumsum[j+1] - cumsum[i]
            if current_sum >= limit:
                break
            if current_sum in prime_set:
                max_consecutive_primes = j - i + 1
                result_prime = current_sum

    return result_prime, max_consecutive_primes


if __name__ == "__main__":
    limit = 1_000_000
    p = Primes(limit)
    primes = p.primes_up_to(limit)
    print(sol(primes, limit))


