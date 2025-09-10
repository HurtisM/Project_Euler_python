# Problem 6
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def squareDiff(N):
    return (sum(i for i in range(N+1))**2 - sum(i**2 for i in range(N+1)))


if __name__ == "__main__":
    print(squareDiff(100))