# Problem 57
# A googol (10^100) is a massive number: one followed by one-hundred zeros;
# 100^100 is almost unimaginably large: one followed by two-hundred zeros.
# Despite their size, the sum of the digits in each number is only 1.
#
# Considering natural numbers of the form, a^b, where a,b < 100,
# what is the maximum digital sum?
def digit_sum(number):
    return sum(int(d) for d in str(number))


def powers(a_lim, b_lim):
    maximum = 0
    for a in range(2, a_lim+1):
        for b in range(2, b_lim+1):
            if digit_sum(a**b) > maximum:
                maximum = digit_sum(a**b)
    return maximum


if __name__ == '__main__':
    print(powers(100, 100))