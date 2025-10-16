class PolygonalNumbers:
    """Triangle, pentagonal, hexagonal numbers, etc."""

    @staticmethod
    def triangle(n):      # T_n = n(n+1)/2
        return n * (n + 1) // 2

    @staticmethod
    def pentagonal(n):    # P_n = n(3n−1)/2
        return n * (3 * n - 1) // 2

    @staticmethod
    def hexagonal(n):     # H_n = n(2n−1)
        return n * (2 * n - 1)
