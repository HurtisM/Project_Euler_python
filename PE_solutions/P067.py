# Problem 67
# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum
# total from top to bottom is 23.
#       3
#      7  4
#    2  4   6
#  8   5  9   3
# that is, 3+7+4+9=23
#
# Find the maximum total from top to bottom of the triangle in file P067input.txt:
# NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem,
# as there are 2^99 altogether! If you could check one trillion (10^12) routes every second it would take over
# twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)
FILE_NAME = "P067input.txt"


def load_data(file_name):
    lines = []
    with open(file_name, "r") as f:
        for line in f:
            lines.append(list(map(int, line.strip().split())))
    return lines


# the solution is exactly the same as for problem 018
def sol(triangle):
    for row in range(len(triangle) - 2, -1, -1):
        for col in range(len(triangle[row])):
            triangle[row][col] = max(int(triangle[row][col]) + int(triangle[row + 1][col]),
                                     int(triangle[row][col]) + int(triangle[row + 1][col + 1]))
    return triangle[0][0]


if __name__ == '__main__':
    data = load_data(FILE_NAME)
    print(sol(data))



