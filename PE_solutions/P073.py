# Problem 73
# Farey sequence: https://en.wikipedia.org/wiki/Farey_sequence

def calc_less_than(x, n):
    a = [int(q*x) for q in range(0,n+1)]
    for q in range(1, n+1):
        m = 2
        while m*q <= n:
            a[m*q] -= a[q]
            m += 1
    return sum(a)-1


if __name__ == '__main__':
    print(calc_less_than(0.5,12000)-calc_less_than(1/3,12000)-1)



