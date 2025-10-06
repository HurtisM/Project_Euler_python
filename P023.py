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


