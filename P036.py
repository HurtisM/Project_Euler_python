# Problem 36
# The decimal number, 585=1001001001 (binary), is palindromic in both bases.
#
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
#
# (Please note that the palindromic number, in either base, may not include leading zeros.)

def is_palindrome(number):
    return str(number) == str(number)[::-1]


def sol(limit=1000000):
    total = 0
    for n in range(1, limit + 1):
        if is_palindrome(n) and is_palindrome(bin(n)[2:]):
            total += n
    return total


if __name__ == "__main__":
    print(sol())
