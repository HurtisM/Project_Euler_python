# Problem 5
# 2025 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def lcm_of_range(n):
    result = 1
    for i in range(1, n + 1):
        result = lcm(result, i)
    return result

if __name__ == "__main__":
    n = 20
    print(f"The smallest positive number divisible by all numbers from 1 to {n} is: {lcm_of_range(n)}")
