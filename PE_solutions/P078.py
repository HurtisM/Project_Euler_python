# Problem 78
# Let p(n) represent the number of different ways in which n coins can be separated into piles.
# For example, five coins can be separated into piles in exactly seven different ways, so p(5)=7.
#
# Find the least value of n for which p(n) is divisible by one million.

MOD = 1_000_000
partitions = [1]  # p(0)=1
n = 1

while True:
    total = 0
    k = 1

    while True:                                 # see Pentagonal Number Theorem recurrence:
                                                # https://en.wikipedia.org/wiki/Pentagonal_number_theorem
        g1 = k * (3*k - 1) // 2                 # generalized pentagonal numbers
        g2 = k * (3*k + 1) // 2

        if g1 > n:                              # till n − g(k) ≥ 0
            break

        sign = -1 if k % 2 == 0 else 1

        total += sign * partitions[n - g1]      # p(n)=p(n−1)+p(n−2)−p(n−5)−p(n−7)+p(n−12)+p(n−15)−p(n−22)−p(n−26)+...
        if g2 <= n:
            total += sign * partitions[n - g2]

        k += 1

    total %= MOD
    partitions.append(total)

    if total == 0:
        print(n)
        break
    n += 1
