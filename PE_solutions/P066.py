# Problem 66
# Diophantine equation
import math

def chakravala(limit):
    maximum_x = 0
    sol = 0
    for N in range(1, limit):
        a = int(math.isqrt(N))
        b = 1
        k = a * a - N

        # perfect square check
        if k == 0:
            continue

        while k != 1:
            # choose m such that (a + b*m) % k == 0
            # and minimize abs(m^2 - N)
            m = None
            m_candidates = []
            for i in range(1, N):
                if (a + b * i) % abs(k) == 0:
                    m_candidates.append(i)
            m = min(m_candidates, key=lambda x: abs(x * x - N))

            # update triple (a, b, k)
            a_next = (a * m + N * b) // abs(k)
            b_next = (a + b * m) // abs(k)
            k_next = (m * m - N) // k

            a, b, k = a_next, b_next, k_next

        if a > maximum_x:
            maximum_x = a
            sol = N
    return sol


if __name__ == '__main__':
    limit = 1000
    print(chakravala(limit))

