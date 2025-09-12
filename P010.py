# Problem 10
# Find the sum of all the primes below two million.


def generate_primes(n):
    primes = []
    is_prime = [True] * n

    for num in range(2, n):
        if is_prime[num]:
            primes.append(num)
            for multiple in range(num * num, n, num):
                is_prime[multiple] = False
    return sum(primes)


if __name__ == "__main__":
    N = 2000000
    print(generate_primes(N))

