# Problem 87
# The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28.
# In fact, there are exactly four numbers below fifty that can be expressed in such a way:
#   28 = 2^2 + 2^3 + 2^4
#   33 = 3^2 + 2^3 + 2^4
#   49 = 5^2 + 3^3 + 2^4
#   47 = 2^2 + 3^3 + 2^4
#
# How many numbers below fifty million can be expressed as the sum of a
# prime square, prime cube, and prime fourth power?

from PE_utils import Primes
p = Primes(10000)

primes = p.primes_up_to(7072)
square = []
cube = []
fourth = []

for p in primes:
    if p**2 < 50_000_000:
        square.append(p**2)
    if p**3 < 50_000_000:
        cube.append(p**3)
    if p**4 < 50_000_000:
        fourth.append(p**4)


# brute force
pocet = set()
for i in square:
    for j in cube:
        for k in fourth:
            if i+j+k <= 50_000_000:
                pocet.add(i+j+k)

print(len(pocet))

# some improovements
pocet = set()
for i in square:
    for j in cube:
        if i+j > 50_000_000:
            break
        for k in fourth:
            if i+j+k <= 50_000_000:
                pocet.add(i+j+k)

print(len(pocet))
