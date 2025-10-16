# Problem 42
# The n-th term of the sequence of triangle numbers is given by, tn = 1/2*n(n+1)
# so the first ten triangle numbers are: 1,3,6,10,15,21,28,36,45,...
#
# By converting each letter in a word to a number corresponding to its alphabetical position and adding these
# values we form a word value. For example, the word value for SKY is 19+11+25=55=t10.
# If the word value is a triangle number then we shall call the word a triangle word.
#
# Using words.txt (P042input.txt'), a 16K text file containing nearly two-thousand common English words,
# how many are triangle words?
FILE_NAME = "P042input.txt"


def load_data(file_name):
    with open(file_name, "r") as f:
        for line in f:
            data = line.strip('"').split('","')
    return sorted(data)


def name_value(name):
    return sum(ord(ch) - 64 for ch in name)


def sol(data_list):
    max_value = max(name_value(name) for name in data_list)

    # precompute triangle numbers up to the largest name value
    tri = set()
    n = 1
    while True:
        t = n * (n + 1) // 2
        if t > max_value:
            break
        tri.add(t)
        n += 1

    # count how many names have triangle values
    return sum(1 for name in data_list if name_value(name) in tri)


if __name__ == "__main__":
    names = load_data(FILE_NAME)
    print(sol(names))

