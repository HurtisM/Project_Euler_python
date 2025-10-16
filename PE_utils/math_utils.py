import time


class MathUtils:
    """General math helpers."""

    @staticmethod
    def is_square(n):
        if n < 0:
            return False
        root = int(n ** 0.5)
        return root * root == n

    @staticmethod
    def gcd(a, b):
        import math
        return math.gcd(a, b)

    @staticmethod
    def lcm(a, b):
        return abs(a * b) // math.gcd(a, b)

    @staticmethod
    def is_palindrome(n):
        s = str(n)
        return s == s[::-1]

    @staticmethod
    def prime_factors_count(n):
        """Return the number of distinct prime factors of n."""
        factors = set()
        # Check 2 separately
        while n % 2 == 0:
            factors.add(2)
            n //= 2
        # Check odd numbers
        i = 3
        while i * i <= n:
            while n % i == 0:
                factors.add(i)
                n //= i
            i += 2
        if n > 1:
            factors.add(n)
        return len(factors)

    @staticmethod
    def prime_factors(n):
        """Return a set of all distinct prime factors of n."""
        factors = set()
        while n % 2 == 0:
            factors.add(2)
            n //= 2
        i = 3
        while i * i <= n:
            while n % i == 0:
                factors.add(i)
                n //= i
            i += 2
        if n > 1:
            factors.add(n)
        return factors

    # ---------- TIMEIT DECORATOR ----------
    @staticmethod
    def timeit(func):
        """Decorator to measure execution time of a function."""

        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f"[Time] {func.__name__} took {end - start:.6f} seconds")
            return result

        return wrapper
