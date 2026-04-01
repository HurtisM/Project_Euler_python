# Problem 82
# In the 5 by 5 matrix below, the minimal path sum by starting in any cell in the left column and finishing
# in any cell in the right column, and only moving up, down and right, is indicated in bold red and is equal to 994.
#
#       131  673 .234 .103  .18
#      .201 .96  .342  965  150
#       630  803  746  422  111
#       537  699  497  121  956
#       805  732  524   37  331
# Find the minimal path sum from the left column to the right column  in p081input.txt
# text file containing an 80 by 80 matrix.

FILE_NAME = "P081input.txt"

def load_data(file_name):
    lines = []
    with open(file_name, "r") as f:
        for line in f:
            lines.append(list(map(int, line.strip().split(","))))
        return lines


def three_way_path_sum(matrix: list[list[int]]) -> int:
    n = len(matrix)

    # začíname prvým stĺpcom
    dp = [matrix[row][0] for row in range(n)]

    for col in range(1, n):
        # krok 1: priamo sprava
        dp = [dp[row] + matrix[row][col] for row in range(n)]

        # krok 2: zhora nadol
        for row in range(1, n):
            dp[row] = min(dp[row], dp[row - 1] + matrix[row][col])

        # krok 3: zdola nahor
        for row in range(n - 2, -1, -1):
            dp[row] = min(dp[row], dp[row + 1] + matrix[row][col])

    return min(dp)



if __name__ == '__main__':
    matrix = load_data(FILE_NAME)
    #matrix = [[131, 673, 234, 103, 18],[201, 96, 342, 965, 150],[630, 803, 746, 422, 111],[537, 699, 497, 121, 956],[805,732, 524, 37, 331]]
    print(three_way_path_sum(matrix))