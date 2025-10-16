def number_divisors(n):
    divisors_count = 1
    current_divisor = 2
    while current_divisor * current_divisor <= n:
        exponent = 0
        while n % current_divisor == 0:
            n //= current_divisor
            exponent += 1
        divisors_count *= (exponent + 1)
        current_divisor += 1
    if n > 1:
        divisors_count *= 2
    return divisors_count


def is_triangel(n):
    return n*(n+1)//2


if __name__ == "__main__":
    n = 1
    while True:
        t = is_triangel(n)
        if number_divisors(t) >= 500:
            print(t)
            break
        n += 1

