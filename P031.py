# Problem 30
#In the United Kingdom the currency is made up of pound (£) and pence (p).
# There are eight coins in general circulation:
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
# It is possible to make £2 in the following way:
#  1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?



coins = [1, 2, 5, 10]


target_amount = 10

ways = [0] * (target_amount + 1)
ways[0] = 1  # There is one way to make 0 pence (using no coins)


for coin in coins:
    for amount in range(coin, target_amount + 1):
        ways[amount] += ways[amount - coin]


num_ways = ways[target_amount]

print("Number of different ways to make £2 using the given coins:", num_ways)
