# Problem 61
from math import ceil, floor, sqrt
from PE_utils.polygons import PolygonalNumbers as P


def polygonal_with_prefix(func, prefix):
    """Generate 4-digit polygonal numbers starting with 'prefix'."""
    n = 1
    while True:
        value = func(n)
        if value > 9999:
            break
        if 1000 <= value <= 9999 and value // 100 == prefix:
            yield value
        n += 1


def sqrt_for_func(func, x):
    """Estimate n from polygonal number formula func(n) = x."""
    # Solve quadratic equations for each polygonal type
    if func == P.triangle:
        return (-1 + sqrt(1 + 8 * x)) / 2
    elif func == P.square:
        return sqrt(x)
    elif func == P.pentagonal:
        return (1 + sqrt(1 + 24 * x)) / 6
    elif func == P.hexagonal:
        return (1 + sqrt(1 + 8 * x)) / 4
    elif func == P.heptagonal:
        return (3 + sqrt(9 + 40 * x)) / 10
    elif func == P.octagonal:
        return (1 + sqrt(1 + 3 * x)) / 3
    else:
        raise ValueError("Unknown polygonal function")

# --------------------------
# Recursive search
# --------------------------
def search_chain(chain, remaining_funcs):
    if not remaining_funcs:
        if chain[-1] % 100 == chain[0] // 100:
            return chain
        return None

    suffix = chain[-1] % 100
    for i, func in enumerate(remaining_funcs):
        for candidate in polygonal_with_prefix(func, suffix):
            result = search_chain(chain + [candidate],
                                  remaining_funcs[:i] + remaining_funcs[i+1:])
            if result:
                return result
    return None


if __name__ == "__main__":
    funcs = [P.triangle, P.square, P.pentagonal, P.hexagonal, P.heptagonal, P.octagonal]

    for start in P.polygonal_in_range(P.triangle, 1000, 9999):
        chain = search_chain([start], [f for f in funcs if f != P.triangle])
        if chain:
            print("Found chain:", chain)
            print("Sum:", sum(chain))
            break
