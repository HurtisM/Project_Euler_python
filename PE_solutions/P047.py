from PE_utils import MathUtils


def find_consecutive_integers():
    consecutive_count = 0
    current_integer = 1

    while consecutive_count < 4:
        if (
            MathUtils.prime_factors_count(current_integer) == 4
            and MathUtils.prime_factors_count(current_integer + 1) == 4
            and MathUtils.prime_factors_count(current_integer + 2) == 4
            and MathUtils.prime_factors_count(current_integer + 3) == 4
        ):
            return current_integer
        else:
            current_integer += 1
    return current_integer

result = find_consecutive_integers()
print("The first of the four consecutive integers:", result)