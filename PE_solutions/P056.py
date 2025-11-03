# Problem 56
# Square Root Convergent

def square_root_expansion(depth):
    num, den = 1, 2  # corresponds to a, b
    count = 0
    for _ in range(depth):
        if len(str(num + den)) > len(str(den)):
            count += 1
        num, den = den, 2 * den + num
    return count


if __name__ == '__main__':
    limit = 1000
    print(square_root_expansion(limit))
