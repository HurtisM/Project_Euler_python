from collections import defaultdict
from PE_utils import Primes

p = Primes(10000)
numbers = p.primes_up_to(10000)

def is_valid(a, b):
    return p.is_prime(int(str(a) + str(b))) and p.is_prime(int(str(b) + str(a)))

connections = defaultdict(set)

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if is_valid(numbers[i], numbers[j]):
            connections[numbers[i]].add(numbers[j])
            connections[numbers[j]].add(numbers[i])


triplets = []
for a in numbers:
    for b in connections[a]:
        for c in connections[a].intersection(connections[b]):
            triplets.append((a, b, c))


quadruplets = []
for (a, b, c) in triplets:
    common = connections[a].intersection(connections[b], connections[c])
    for d in common:
        quadruplets.append((a, b, c, d))


quintuplets = []
for (a, b, c, d) in quadruplets:
    common = connections[a].intersection(connections[b], connections[c], connections[d])
    for e in common:
        quintuplets.append((a, b, c, d, e))


min_sum = min(sum(q) for q in quintuplets)
print(min_sum)

from PE_utils import Primes
from collections import defaultdict

# --- Step 1: prepare primes ---
p = Primes(10000)
primes = p.primes_up_to(10000)


def is_valid(a, b):
    """Check if both concatenations of a and b are prime."""
    return p.is_prime(int(str(a) + str(b))) and p.is_prime(int(str(b) + str(a)))


# --- Step 2: build compatibility graph ---
connections = defaultdict(set)
for i in range(len(primes)):
    for j in range(i + 1, len(primes)):
        if is_valid(primes[i], primes[j]):
            connections[primes[i]].add(primes[j])
            connections[primes[j]].add(primes[i])


# --- Step 3: recursive clique finder ---
def extend_clique(current):
    """Recursively extend a clique of mutually compatible primes."""
    if len(current) == 5:
        yield current
        return

    # Only keep primes that are compatible with *all* in current
    common = set.intersection(*(connections[n] for n in current))
    # To avoid permutations (same set in different order)
    for nxt in sorted(common):
        if nxt > current[-1]:
            yield from extend_clique(current + [nxt])


# --- Step 4: try starting from each prime ---
solutions = []
for prime in primes:
    for result in extend_clique([prime]):
        solutions.append(result)
        print("Found:", result, "sum:", sum(result))

# --- Step 5: get the minimal sum ---
if solutions:
    print("Lowest sum:", min(sum(s) for s in solutions))
else:
    print("No solution found.")