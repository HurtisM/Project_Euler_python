from math import isqrt


def continued_fraction_sqrt(N):
    """
    Returns continued fraction of sqrt(N) in form [a0;(a1,a2,...)], period length
    """
    a0 = isqrt(N)
    if a0 * a0 == N:
        return [a0], 0  # perfect square

    m, d, a = 0, 1, a0
    period_list = []

    while True:
        m = d * a - m
        d = (N - m * m) // d
        a = (a0 + m) // d
        period_list.append(a)
        if a == 2 * a0:  # period complete
            break

    return [a0, tuple(period_list)], len(period_list)


pocet = 0

for i in range(1, 10001):
    cf, lenght = continued_fraction_sqrt(i)
    if lenght % 2 == 1:
        pocet += 1

print(pocet)



