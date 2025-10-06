# Problem 23
# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example,
# the sum of the proper divisors of 28 would be 1+2+4+7+14 = 28, which means that 28 is a perfect number.
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant
# if this sum exceeds n.
#
# As 12 is the smallest abundant number, 1+2+3+4+6=16, the smallest number that can be written as the sum of
# two abundant numbers is 24.
# By mathematical analysis, it can be shown that all integers greater than 28123 can be written
# as the sum of two abundant numbers.
# However, this upper limit cannot be reduced any further by analysis even though it is known that the
# greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
#
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.


import math


def find_non_abundant_sum(upper_limit):
    numbers = abundant(upper_limit)
    sum_numbers = [False] * (upper_limit + 1)
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            abundant_sum = numbers[i] + numbers[j]
            if abundant_sum <= upper_limit:
                sum_numbers[abundant_sum] = True
            else:
                break
    non_abundant_sum = sum(i for i, is_sum in enumerate(sum_numbers) if not is_sum)
    return non_abundant_sum


def abundant(upper_limit):

    list_of_abundant = []
    for i in range(12, upper_limit):
        if div_sum(i) > i:
            list_of_abundant.append(i)
    return list_of_abundant


def div_sum(num):
    result = 0
    i = 2
    while i <= math.sqrt(num):
        if num % i == 0:
            if i == num /i:
                result += i
            else:
                result += (i + num/i)
        i += 1
    return result+1


if __name__ == "__main__":
    limit = 28123
    print(find_non_abundant_sum(limit))


