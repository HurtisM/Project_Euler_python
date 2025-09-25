#Problem 21
#Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
#If d(a)=b and d(b)=a, where a!=b, then a and b are an amicable pair and each of a and a are called amicable numbers.
#For example, the proper divisors of 220 are 1,2,4,5,10,11,20,22,44,55,110  therefor d(220)= 284
#the proper divisor of 284 are 1,2,4,71,142 so d(284)=220

#Evaluate the sum of all the amicable numbers under 10.000

import math


def divSum(num):
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


def amicable_numbers(limit):
    pairs = []
    amicable = ()
    for n in range(limit):
        div = int(divSum(n))
        if (div, n) in pairs:
            amicable += (n, div)
        pairs.append((n, div))
    return amicable


if __name__ == "__main__":
    N = 10000
    print(sum(amicable_numbers(N)))

