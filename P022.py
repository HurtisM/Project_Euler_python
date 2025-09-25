#Problem 22
#Using P022input.txt text file containing over five-thousand first names, begin by sorting it into alphabetical order.
# Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list
# to obtain a name score.

#For example, when the list is sorted into alphabetical order, COLIN, which is worth 3+15+12+9+14=53,
#s the 938th name in the list. So, COLIN would obtain a score of 938x53=49714
#What is the total of all the name scores in the file?
FILE_NAME = "P022input.txt"


def load_data(file_name):
    data = ()
    with open(file_name, "r") as f:
        for line in f:
            data = line.strip('"').split('","')
    return sorted(data)


def name_value(name):
    value = 0
    for ch in name:
        value += ord(ch) - 64
    return value


if __name__ == "__main__":
    names = load_data(FILE_NAME)

    total = 0
    for i, name in enumerate(names):
        total += (i + 1) * name_value(name)
    print(total)

