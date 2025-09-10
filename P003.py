def largest_prime_factor(n):
    lpf = 0
    divisor = 2
    while divisor <= n:
        if n % divisor == 0:
            lpf = divisor
            n = n // divisor
        else:
            divisor += 1
    return lpf


if __name__ == "__main__":
    number_to_factorize = 5
    print(f"Largest prime factor of {number_to_factorize}: {largest_prime_factor(number_to_factorize)}")
