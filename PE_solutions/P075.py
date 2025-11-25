# Problem 75

from math import gcd

def all_right_triangles(L):
    memo = {}
    # Generate primitive triples using Euclid's formula
    m = 2
    while True:
        # smallest possible perimeter from this m: 2m(m+1)
        if 2 * m * (m + 1) > L:
            break
        for n in range(1, m):
            # must have opposite parity and gcd = 1
            if (m - n) % 2 == 1 and gcd(m, n) == 1:
                # primitive triple
                a = m*m - n*n
                b = 2*m*n
                c = m*m + n*n
                p = a + b + c

                if p > L:
                    continue
                # generate all multiples of the primitive triple
                k = 1
                while k * p <= L:
                    triple = (a*k, b*k, c*k)
                    memo.setdefault(k * p, []).append(triple)
                    k += 1
        m += 1
    return memo


def sol(N):
    triangles = all_right_triangles(N)
    count = 0
    for element in triangles:
        if len(triangles[element]) == 1:
            count += 1
    return count


if __name__ == '__main__':
    limit = 1_500_000
    print(sol(limit)
          )

