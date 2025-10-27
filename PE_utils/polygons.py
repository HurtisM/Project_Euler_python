import math


class PolygonalNumbers:
    """Generate and check triangle, square, pentagonal, hexagonal, heptagonal, and octagonal numbers."""

    # ------------------------------
    # Polygonal number generators
    # ------------------------------
    @staticmethod
    def triangle(n):
        """Tₙ = n(n + 1)/2"""
        return n * (n + 1) // 2

    @staticmethod
    def square(n):
        """Sₙ = n²"""
        return n * n

    @staticmethod
    def pentagonal(n):
        """Pₙ = n(3n − 1)/2"""
        return n * (3 * n - 1) // 2

    @staticmethod
    def hexagonal(n):
        """Hₙ = n(2n − 1)"""
        return n * (2 * n - 1)

    @staticmethod
    def heptagonal(n):
        """Hpₙ = n(5n − 3)/2"""
        return n * (5 * n - 3) // 2

    @staticmethod
    def octagonal(n):
        """Oₙ = n(3n − 2)"""
        return n * (3 * n - 2)

    # ------------------------------
    # Range generator
    # ------------------------------
    @staticmethod
    def polygonal_in_range(func, start, end):
        """
        Generate all polygonal numbers in the range [start, end].
        'func' is a generator like PolygonalNumbers.triangle, etc.
        """
        n = 1
        results = []
        while True:
            value = func(n)
            if value > end:
                break
            if value >= start:
                results.append(value)
            n += 1
        return results

    # ------------------------------
    # Polygonal number checkers
    # ------------------------------
    @staticmethod
    def is_triangle(x):
        n = (math.sqrt(8 * x + 1) - 1) / 2
        return n.is_integer()

    @staticmethod
    def is_square(x):
        return int(math.isqrt(x)) ** 2 == x

    @staticmethod
    def is_pentagonal(x):
        n = (1 + math.sqrt(24 * x + 1)) / 6
        return n.is_integer()

    @staticmethod
    def is_hexagonal(x):
        n = (1 + math.sqrt(8 * x + 1)) / 4
        return n.is_integer()

    @staticmethod
    def is_heptagonal(x):
        n = (3 + math.sqrt(40 * x + 9)) / 10
        return n.is_integer()

    @staticmethod
    def is_octagonal(x):
        n = (1 + math.sqrt(3 * x + 1)) / 3
        return n.is_integer()

    @staticmethod
    def is_polygonal(x, s):
        """
        Generic checker for s-gonal numbers (s ≥ 3).
        Formula: n = (sqrt(8*(s-2)*x + (s-4)**2) + (s-4)) / (2*(s-2))
        """
        n = (math.sqrt(8 * (s - 2) * x + (s - 4) ** 2) + (s - 4)) / (2 * (s - 2))
        return n.is_integer()
