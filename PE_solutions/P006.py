# Problem 6
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
import timeit

def squareDiff(N):
    return (sum(i for i in range(N+1))**2 - sum(i**2 for i in range(N+1)))

def sq_diff_formula(n):
    sq_of_sum = (n*(n+1) // 2)**2
    sum_of_sq = n * (n+1) * (2* n+1) // 6
    return sq_of_sum - sum_of_sq


if __name__ == "__main__":
    time_brute = timeit.timeit(lambda:squareDiff(1000000), number = 100 )
    time_formula = timeit.timeit(lambda:sq_diff_formula(1000000), number = 100 )

    print(f"brute force time: {time_brute:.6f} seconds")
    print(f"using formula time: {time_formula:.6f} seconds")