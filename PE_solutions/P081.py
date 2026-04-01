# Problem 81
# In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right,
# by only moving to the right and down, is indicated in bold red and is equal to 2427.
#
#       .131  673  234  103   18
#       .201  .96 .342  965  150
#        630  803 .746 .422  111
#        537  699  497 .121  956
#        805  732  524  .37 .331
#
# Find the minimal path sum from the top left to the bottom right by only moving right and down in p081input.txt
# text file containing an 80 by 80 matrix.

FILE_NAME = "P081input.txt"

def load_data(file_name):
    lines = []
    with open(file_name, "r") as f:
        for line in f:
            lines.append(list(map(int, line.strip().split(","))))
        return lines

def min_path_sum(matrix):
    n = len(matrix)

    min_sum_matrix = [[0] * n for _ in range(n)]

    min_sum_matrix[0][0] = matrix[0][0]
    for i in range(1, n):
        min_sum_matrix[i][0] = min_sum_matrix[i-1][0] + matrix[i][0]
        min_sum_matrix[0][i] = min_sum_matrix[0][i - 1] + matrix[0][i]

    #
    for i in range(1, n):
        for j in range(1, n):
            min_sum_matrix[i][j] = matrix[i][j] + min(min_sum_matrix[i-1][j], min_sum_matrix[i][j-1])

    return min_sum_matrix[n - 1][n - 1]


if __name__ == '__main__':
    matrix = load_data(FILE_NAME)
    print(min_path_sum(matrix))

