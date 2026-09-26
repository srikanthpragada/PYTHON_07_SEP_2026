def ispassed(n):
    return n > 50


nums = [50, 55, 90, 23, 45]

for n in map(ispassed, nums):
    print(n)
