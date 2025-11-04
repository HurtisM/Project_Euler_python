# Problem 62
# The cube, 41063625 (345^3), can be permuted to produce two other cubes:56623104 (384^3)
# and 66430125 (405^3). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits
# which are also cube.
#
# Find the smallest cube for which exactly five permutations of its digits are cube.
from collections import defaultdict
from PE_utils.math_utils import MathUtils


def get_hash_rep(n):
    return ",".join(sorted(list(str(n))))


def cube_key(n: int) -> str:
    return ''.join(sorted(str(n)))


@MathUtils.timeit
def sol1():
    cubes = {}
    i = 345
    while True:
        hash_rep = get_hash_rep(i ** 3)
        cubes.setdefault(hash_rep, []).append(i)
        if len(cubes[hash_rep]) == 5:
            break
        i += 1
    ans = min(cubes[hash_rep]) ** 3
    return ans


@MathUtils.timeit
def sol2():
    cubes = defaultdict(list)
    i = 1
    while True:
        key = cube_key(i**3)
        cubes[key].append(i)
        if len(cubes[key]) == 5:
            return cubes[key][0]**3
        i += 1


if __name__ == '__main__':
    print(sol1())
    print(sol2())


# first version which worked but was very slow
'''def is_permutation(number1, number2):
    return sorted(str(number1)) == sorted(str(number2))

# zoznam kociek a ich objemu
cubes = []

for i in range(5000,10000):
    cubes.append((i,i**3))

# ak jeden objem je permutacia druheho, pridame ho do listu
#
zoznamy = []
for m in range(len(cubes)):
    list_perm = [cubes[m]]
    for n in range(m+1,len(cubes)):
        if is_permutation(cubes[m][1],cubes[n][1]):
            list_perm.append(cubes[n])
    zoznamy.append(list_perm)
    list_perm = []

for item in zoznamy:
    if len(item) == 5:
        print(item)  '''