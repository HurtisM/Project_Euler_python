#Problem 27

# input
# we are loking for X for which equation n^2 + a*n + b  is prime for all n in range 0...X
# we have limit for b so we can say for n=0 b has to be prime, so we are considering only primes <= limit

def prime(limit):                    #generate list of primes less than limit
    result = []
    sieve = [True for i in range(limit + 1)]
    for b in range(4, limit + 2, 2):
        sieve[b] = False
    a = 3
    while a ** 2 <= limit:
        if sieve[a]:
            for b in range(a ** 2, limit + 1, a):
                sieve[b] = False
        a += 2
    for a in range(2, limit + 1):
        if sieve[a]:
            result.append(a)
    return result


def sol(limit):
    primes = prime(limit)
    n_max, a_max, b_max = 0, 0, 0
    for a in range(-999, 1000):
        for b in primes:
            n = 0
            while True:
                if (abs(n ** 2 + n * a + b)) not in primes:
                    if n > n_max:
                        n_max = n
                        a_max = a
                        b_max = b
                    break
                n += 1
    return n_max, a_max, b_max


if __name__ == '__main__':
    b_limit = 1000
    n_naj, a_naj, b_naj = (sol(b_limit))
    print(f"Rovnica: n^2 {a_naj}n + {b_naj}")
    print("Vygenerovanych prvocisel:", n_naj)
    print("Vysledok:", a_naj * b_naj)
