#Problem 1
#If we list all the natural numbers below 10 that are multiples of 3 or 5,
#we get 3,5,6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

import timeit
#brute force:
def multiples(n):
    sum = 0
    for i in range(3,n):
        if i%3 == 0 or i%5 == 0:
            sum += i
    return sum


# faster solution with no divisions
def multiples_no_divisions(n):
    sum = 0
    start = 3
    while start < n:
        sum += start
        start += 3
    start = 5
    while start < n:
        sum += start
        start += 15
    start = 10
    while start < n:
        sum += start
        start += 15
    return sum

if __name__ == "__main__":
    print(multiples(1000))
    print(multiples_no_divisions(1000))
