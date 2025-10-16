# Problem 7
# By listing the first six prime numbers: 2,3,5,7,11,13, we can see that the 6th prime is 13
# What is the 10001 prime number?
def generate_primes(n):
    primes = []
    is_prime = [True] * (n*20)

    for num in range(2, n*20):
        if is_prime[num]:
            primes.append(num)
            for multiple in range(num * num, n*20, num):
                is_prime[multiple] = False
            if len(primes) == n:
                break
    return primes[-1]


if __name__ == "__main__":
    N = 10001
    print(f"The {N} th prime number is: {generate_primes(N)}")
