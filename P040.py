# Problem 40
#  An irrational decimal fraction is created by concatenating the positive integers:
#           0.123456789101112131415161718192021
# It can be seen that the 12th digit of the fractional part is 1.
#
# If dn represents the n-th digit of the fractional part, find the value of the following expression.
# d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000
import timeit


def sol():
    suma = 1
    digit = 0
    indexes = (1, 10, 100, 1000, 10000, 100000, 1000000)
    for i in range(1, 1000000):
        for j in range(len(str(i))):
            digit += 1
            if digit in indexes:
                suma *= int(str(i)[j])
    return suma


def sol2():
    indexes = [1, 10, 100, 1000, 10000, 100000, 1000000]
    result = 1
    current_length = 0
    n = 1

    for target in indexes:
        while True:
            s = str(n)
            if current_length + len(s) >= target:
                result *= int(s[target - current_length - 1])
                current_length += len(s)
                break
            current_length += len(s)
            n += 1
        n += 1
    return result


if __name__ == "__main__":
    print(sol())
    print(sol2())

''' # first solution is ~ 42x slower
    time_sol = timeit.timeit(lambda: sol(), number=1)
    time_sol2 = timeit.timeit(lambda: sol2(), number=1)

    print(f"sol time: {time_sol:.6f} seconds")
    print(f"sol2 time: {time_sol2:.6f} seconds")
'''