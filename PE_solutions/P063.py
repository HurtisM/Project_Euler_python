# Problem 63
# The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the
# 9-digit number, 134217728 = 8^9, is a ninth power.
#
# How many n-digit positive integers exist which are also an n-th power?
from PE_utils.math_utils import MathUtils


@MathUtils.timeit
def sol1():
    sucet = 0
    for j in range(1,10):
        pocet = 0
        for i in range(1,35):
            a = j**i
            if len(str(a)) == i:
                pocet += 1
        print(f'{j} = {pocet}')
        sucet += pocet
    return sucet


@MathUtils.timeit
def sol():
    total = 0
    for base in range(1, 10):  # 10^n always has n+1 digits
        if base == 1:
            print("1 = 1")
            total += 1
            continue
        count = 0
        power = 1
        while True:
            num = base ** power
            if len(str(num)) == power:
                count += 1
            elif len(str(num)) < power:
                break  # once length < power, it will stay < for larger powers
            power += 1
        print(f"{base} = {count}")
        total += count
    return total


if __name__ == '__main__':
    print(sol1())
    print(sol())
