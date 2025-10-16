# Problem 38
#Take the number 192 and multiply it by each of 1, 2, and 3:
# 192x1=192
# 192x2=384
# 192x3=579
# By concatenating each product we get the 1 to 9 pandigital, 192384579. We will call
# the concatenated product of 192 and (1,2,3).
# The same can be achieved by starting with 9 and multiplying by 1,2,3,4, and 5,
# giving the pandigital, 918273645, which is the concatenated product of
# 9 and (1,2,3,4,5).
# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated
# product of an integer with (1,2,...,n) where n>1 ?
def is_1_to_9_pandigital(s):
    return len(s) == 9 and set(s) == set('123456789')


def largest_concatenated_pandigital():
    # digit length 4..
    d = 4
    for k in range(10**d - 1, 10**(d-1) - 1, -1):
        s = str(k)
        if '0' in s:
            continue
        if len(set(s)) != len(s):             # skip bases with repeated digits
            continue
        concat = ""
        i = 1
        while len(concat) < 9:
            concat += str(k * i)
            i += 1
        if is_1_to_9_pandigital(concat):
            return int(concat), k, i-1
    return None


if __name__ == "__main__":
    print(largest_concatenated_pandigital())