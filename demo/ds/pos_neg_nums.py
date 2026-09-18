# Take numbers until 0 and display pos first and then negative

nums = []

while True:
    n = int(input("Enter a number [0 to stop] :"))
    if n == 0:
        break
    nums.append(n)

# Print positive numbers
for n in nums:
    if n > 0:
        print(n)

# Print negative numbers
for n in nums:
    if n < 0:
        print(n)
