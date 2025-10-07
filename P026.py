def count_repeat(number):
    # For denominators with factors of 2 or 5, the decimal terminates
    while number % 2 == 0:
        number //= 2
    while number % 5 == 0:
        number //= 5
    if number == 1:
        return 0  # no repeating cycle
    # Now, find the smallest k
    remainder = 10 % number
    k = 1
    while remainder != 1:
        remainder = (remainder * 10) % number
        k += 1
    return k


def longest_recurring(limit):
    longest = 0
    number = 0
    for i in range(1, limit+1):
        if count_repeat(i) > longest:
            longest = count_repeat(i)
            number = i
    return number


if __name__ == '__main__':
    print(longest_recurring(1000))
