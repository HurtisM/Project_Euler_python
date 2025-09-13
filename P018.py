# Problem 18
# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum
# total from top to bottom is 23.
#       3
#      7  4
#    2  4   6
#  8   5  9   3
# that is, 3+7+4+9=23
#
# Find the maximum total from top to bottom of the triangle in file P018input.txt:
#
# NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route.
# However, Problem 67, is the same challenge with a triangle containing one-hundred rows;
# it cannot be solved by brute force, and requires a clever method! ;o)
FILE_NAME = "P018input.txt"


def load_data(file_name):
    lines = []
    with open(file_name, "r") as f:
        for line in f:
            lines.append(list(map(int, line.strip().split())))
    return lines


if __name__ == "__main__":
    lines = load_data(FILE_NAME)

    for r in range(len(lines) - 2, -1, -1):
        for c in range(len(lines[r])):
            lines[r][c] = max(int(lines[r][c]) + int(lines[r + 1][c]), int(lines[r][c]) + int(lines[r + 1][c + 1]))
    print(lines[0][0])


