# Problem 32
# We shall say that an n-digit number is pandigital if it makes use of all the digits
#  1 to n exactly once; for example, the 5-digit number, 15423, is 1 through 5 pandigital.
#
# The product 7524 is unusual, as the identity, 39 x 186 = 7254, containing multiplicand, multiplier, and product
# is 1 through 9 pandigital.
#
# Find the sum of all products whose multiplicand/multiplier/product identity
# can be written as a 1 through 9 pandigital.
#
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
def is_pandigital_1_to_9(s):
    return len(s) == 9 and set(s) == set("123456789")


def find_pandigital_products():
    products = set()
    # Case 1: 1-digit × 4-digit = 4-digit
    for i in range(1, 10):
        for j in range(1234, 9877):  # 4-digit numbers
            p = i * j
            combined = f"{i}{j}{p}"
            if is_pandigital_1_to_9(combined):
                products.add(p)

    # Case 2: 2-digit × 3-digit = 4-digit
    for i in range(12, 100):  # 2-digit numbers
        for j in range(123, 988):  # 3-digit numbers
            p = i * j
            combined = f"{i}{j}{p}"
            if is_pandigital_1_to_9(combined):
                products.add(p)
    return products


if __name__ == '__main__':
    pandigital_products = find_pandigital_products()
    print("Sum of unique products:", sum(pandigital_products))
