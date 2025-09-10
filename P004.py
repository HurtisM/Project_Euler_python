# Problem 4
# A palindromic number reads the same both ways. The largest palindrome made from the product of two
# 2-digit numbers is 9009 = 99x91
# Find the largest palindrome made from the product of two 3-digit numbers

def isPalindrome(number):
    if str(number) == str(number)[::-1]:
        return True
    return False


def solution():
    for m in range(999, 900, -1):
        for n in range(m, 900, -1):
            if isPalindrome(m * n):
                return m*n


if __name__ == "__main__":
    print(solution())

