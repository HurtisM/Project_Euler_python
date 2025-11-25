# Problem 74

from math import factorial

# Precompute factorials of digits 0–9
fact = [factorial(i) for i in range(10)]

def fact_digit_sum(n):
    s = 0
    while n > 0:
        n, d = divmod(n, 10)
        s += fact[d]
    return s

# memo table to store known chain lengths
memo = {}

def chain_length(n):
    visited = []       # stores numbers in this chain
    seen = set()

    while n not in seen:
        if n in memo:  # we know the rest of the chain
            total_length = len(visited) + memo[n]
            break
        visited.append(n)
        seen.add(n)
        n = fact_digit_sum(n)
    else:
        # we hit a loop inside this chain
        loop_start = visited.index(n)
        loop_len = len(visited) - loop_start
        # everything in the loop gets same loop length
        for x in visited[loop_start:]:
            memo[x] = loop_len
        # everything before the loop gets decreasing lengths
        total_length = len(visited)

    # store remaining values with correct lengths
    extra = total_length
    for x in visited:
        if x not in memo:
            memo[x] = extra
        extra -= 1

    return total_length


count = 0
for i in range(1_000_000):
    if chain_length(i) == 60:
        count += 1

print(count)
