
def sum_of(lines):
    sum = 0
    for line in lines:
        sum += int(line)
    return str(sum)[:10]


if __name__ == "__main__":
    with open("P013input.txt", "r") as file:
        lines = file.readlines()

    print(sum_of(lines))

