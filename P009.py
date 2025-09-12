# Problem 9
import timeit

def brute_force():
    for a in range(1, 332 + 1):
        for b in range(a+1, int((1000-a)/2)):
            c = 1000 - a - b
            if a**2 + b**2 == c**2:
                return a*b*c
    return None


def formula():
    for m in range(2, 23):
        for n in range(0, m-1):
            if m*(m+n) == 500:
                return 2*m*n*(m**2 - n**2)
    return None


if __name__ == "__main__":
    time_brute = timeit.timeit(lambda: brute_force(), number=100)
    time_formula = timeit.timeit(lambda: formula(), number=100)

    print(f"Brute force time: {time_brute:.6f} seconds")
    print(f"Formula time: {time_formula:.6f} seconds")