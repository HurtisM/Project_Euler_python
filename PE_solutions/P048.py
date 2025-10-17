# Problem 48
# The series, 1^1+2^2+3^3+...+10^10.
#
# Find the last ten digits of the series, 1^1+2^2+3^3+...+1000^1000.
def last_ten_digits_self_powers(n=1000):
    mod = 10**10
    total = 0
    for i in range(1, n+1):
        total = (total + pow(i, i, mod)) % mod
    # return as zero-padded 10-digit string
    return f"{total:010d}"

if __name__ == "__main__":
    print(last_ten_digits_self_powers(1000))


