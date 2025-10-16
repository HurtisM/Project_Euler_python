from itertools import combinations_with_replacement


def make_combos(length):
    return [list(c) for c in combinations_with_replacement(range(10), length)]


def solution():
    result = 0
    for length in range(4, 7):  # lengths 4, 5, 6
        combos = make_combos(length)
        for combo in combos:
            pow_sum = sum(d ** 5 for d in combo)
            num_digits = [int(d) for d in str(pow_sum)]
            if sorted(num_digits) == sorted(combo):
                result += pow_sum
    return result


if __name__ == '__main__':
    print(solution())
