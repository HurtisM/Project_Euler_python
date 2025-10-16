# Problem 16
# What is the sum of the digits of the number 2^100?

str = str(2**1000)

sum = 0
for char in str:
    sum += int(char)

print(sum)