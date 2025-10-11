# Problem 39
# If p is the perimeter of a right angle triangle with integral length sides, {a, b, c},
# there are exactly three solutions for p=120. {20,48,52}, {24,45,51},{30,40,50}
#
# For which value ofp<=1000, is the number of solutions maximised?
from math import sqrt


def sol(lim):
    perimeters = [0] * lim

    for a in range(500, 5, -1):
        for b in range(a, 4, -1):
            c = sqrt(a ** 2 - b ** 2)
            if c.is_integer():
                per = (a + b + int(c))
                if per < lim:
                    perimeters[per] += 1
    return perimeters.index(max(perimeters))


if __name__ == "__main__":
    limit = 1000
    print(sol(limit))
