# P053
from PE_utils.math_utils import MathUtils

@MathUtils.timeit
def sol(limit, number):
    triangle = [[0 for _ in range(limit+1)] for _ in range(limit+1)]
    count = 0
    for a in range(limit+1):
        triangle[a][0] = 1
        triangle[a][a] = 1
    for row in range(1, limit+1):
        for col in range(1, row):
            triangle[row][col] = triangle[row-1][col] + triangle[row-1][col-1]
            if triangle[row][col] > number:
                count += 1
    return count


@MathUtils.timeit
def sol2(limit, number):
    prev_row = [1]
    count = 0

    for n in range(1, limit + 1):
        row = [1]
        for k in range(1, n):
            val = prev_row[k - 1] + prev_row[k]
            if val > number:
                count += 1
                val = number + 1
            row.append(val)
        row.append(1)
        prev_row = row

    return count

if __name__ == "__main__":
    print(sol(100, 1000000))
    print(sol2(100, 1000000))

