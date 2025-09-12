import math
import timeit


# binomicka funkcia , trochu zlozite funguje len pr mriezky m x n, ale vstup funkce je (prvy argument m+n, druhy argument m alebo n )
def binom(n, m):
    if m < 0 or m > n:
        return 0
    b = [0] * (n + 1)
    b[0] = 1
    for i in range(1, n + 1):
        b[i] = 1
        j = i - 1
        while j > 0:
            b[j] += b[j - 1]
            j -= 1
    return b[m]


def binom2(n, k):
    if k > n - k:
        k = n - k
    result = 1
    for i in range(1, k + 1):
        result = result * (n - i + 1) // i
    return result


def grid_paths(n, m):
    return binom(n+m, n)

def grid_paths2(n, m):
    return binom2(n+m, n)


if __name__ == "__main__":
    time_b1 = timeit.timeit(lambda: grid_paths(20,20), number=10000)
    time_b2 = timeit.timeit(lambda: grid_paths2(20, 20), number=10000)

    print(f"Binom 1 func time: {time_b1:.6f} seconds")
    print(f"Binom 2 func time: {time_b2:.6f} seconds")

    print(grid_paths(20, 20))
    print(grid_paths2(20, 20))