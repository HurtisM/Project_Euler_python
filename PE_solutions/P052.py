# Problem 52
# It can be seen that the number, 125874, and its double, 251748,
# contain exactly the same digits, but in a different order.
#
# Find the smallest positive integer, x, such that
# 2x, 3x, 4x, 5x, and 6x, contain the same digits.

def sol():
    for num_of_digits in range(3, 10):
        start = 10 ** (num_of_digits - 1)
        end = int("1" + "6" * (num_of_digits - 1))
        for n in range(start, end + 1):
            if all(set(str(i * n)) == set(str(n)) for i in range(2, 7)):
                return n


if __name__ == "__main__":
    print(sol())

