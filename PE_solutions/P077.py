# Problem 76
# It is possible to write ten as the sum of primes in exactly five different ways:
# 7+3
# 5+5
# 5+3+2
# 3+3+2+2
# 2+2+2+2+2
# What is the first value which can be written as the sum of primes in over five thousand different ways?

from PE_utils import Primes
p = Primes(10000)


def num_ways(number):                   #same approach as in problem 31 (coins sum)
    primes = p.primes_up_to(number)
    target_amount = number

    ways = [0] * (target_amount + 1)
    ways[0] = 1  # There is one way to make 0

    for prime in primes:
        for amount in range(prime, target_amount + 1):
            ways[amount] += ways[amount - prime]
    return ways[target_amount]


if __name__ == '__main__':
    limit = 5000
    for num in range(10, 100):
        if num_ways(num) > limit:
            print(num)
            break
    print("Range too narrow!")
