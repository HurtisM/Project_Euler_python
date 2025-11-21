# Problem 71
# Farey sequence: https://en.wikipedia.org/wiki/Farey_sequence
# if a/b and c/d are neighbours in a Farey sequence then the first term that appears
# between them as the order of the Farey sequence is incremented is a+c/b+d
# which first appears in the Farey sequence of order b + d
# so try while b+d < 1000000....

def fractions(lim, a=2, b=5, c=3, d=7):
    while b+d <= lim:
        a = a + c
        b = b + d
    return a, b


if __name__ == '__main__':
    limit = 1000000
    print(fractions(limit))
