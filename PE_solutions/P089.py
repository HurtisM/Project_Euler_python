# Problem 89
# For a number written in Roman numerals to be considered valid there are basic rules which must be followed.
# Even though the rules allow some numbers to be expressed in more than one way
# there is always a "best" way of writing a particular number.
# For example, it would appear that there are at least six ways of writing the number sixteen:
#
# IIIIIIIIIIIIIIII
# VIIIIIIIIIII
# VVIIIIII
# XIIIIII
# VVVI
# XVI
#
# However, according to the rules only XIIIIII and XVI are valid, and the last example is considered
# to be the most efficient, as it uses the least number of numerals.
# The text file, P089input.txt, contains one thousand numbers written in valid, but not necessarily minimal,
# Roman numerals.
#
# Find the number of characters saved by writing each of these in their minimal form.
# Note: You can assume that all the Roman numerals in the file contain no more than four consecutive identical units.
# input from file
FILE_NAME = "P089input.txt"


def load_data(file_name):
    romans = []
    with open(file_name, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                romans.append(line)
    return romans

def roman_to_int(roman):
    values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    allowed_subtractions = {
        'I': ['V', 'X'],
        'X': ['L', 'C'],
        'C': ['D', 'M']
    }

    total = 0

    for i in range(len(roman)):
        if i + 1 < len(roman) and values[roman[i]] < values[roman[i + 1]]:

            # validacia
            if roman[i] not in allowed_subtractions or \
               roman[i + 1] not in allowed_subtractions[roman[i]]:
                return None

            total -= values[roman[i]]
        else:
            total += values[roman[i]]

    return total

def int_to_roman(num):
    roman_map = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')
    ]

    result = []

    for value, symbol in roman_map:
        while num >= value:
            result.append(symbol)
            num -= value

    return ''.join(result)


if __name__ == '__main__':
    data = load_data(FILE_NAME)

    saved = 0

    for item in data:
        number = roman_to_int(item)

        minimal = int_to_roman(number)

        saved += len(item) - len(minimal)


    print(saved)

