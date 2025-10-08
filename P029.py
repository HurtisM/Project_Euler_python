# Problem 29

def distinct_powers(a_lim, b_lim):
    powers = []
    for a in range(2, a_lim+1):
        for b in range(2, b_lim+1):
            if a**b not in powers:
                powers.append(a**b)
    return len(powers)


if __name__ == '__main__':
    print(distinct_powers(100, 100))
