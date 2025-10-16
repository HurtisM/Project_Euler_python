# Problem 11
# What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally)
# in the 20x20 grid?
# for this problem the input data are stored in file P011input.txt
def find_max_product(array):
    max_product = 0

    # Check horizontally
    for i in range(20):
        for j in range(17):
            product = array[i][j] * array[i][j+1] * array[i][j+2] * array[i][j+3]
            max_product = max(max_product, product)

    # Check vertically
    for i in range(17):
        for j in range(20):
            product = array[i][j] * array[i+1][j] * array[i+2][j] * array[i+3][j]
            max_product = max(max_product, product)

    # Check diagonally (top-left to bottom-right)
    for i in range(17):
        for j in range(17):
            product = array[i][j] * array[i+1][j+1] * array[i+2][j+2] * array[i+3][j+3]
            max_product = max(max_product, product)

    # Check diagonally (top-right to bottom-left)
    for i in range(17):
        for j in range(3, 20):
            product = array[i][j] * array[i+1][j-1] * array[i+2][j-2] * array[i+3][j-3]
            max_product = max(max_product, product)

    return max_product


if __name__ == "__main__":
    with open("P011input.txt", "r") as file:
        lines = file.readlines()

    grid = [list(map(int, line.split())) for line in lines]

    print(f"The maximum product of 4 adjacent numbers is: {find_max_product(grid)}")
