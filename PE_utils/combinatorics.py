import math


class Combinatorics:
    """Factorials, nCr, permutations, etc."""

    @staticmethod
    def factorial(n):
        return math.factorial(n)

    @staticmethod
    def nCr(n, r):
        if r > n or n < 0 or r < 0:
            return 0
        return math.comb(n, r)

    @staticmethod
    def nPr(n, r):
        if r > n or n < 0 or r < 0:
            return 0
        return math.perm(n, r)
