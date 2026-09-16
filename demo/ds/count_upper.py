# Take a string and count how many uppercase letter are in the string

s = input("Enter a string :")

count = 0
for c in s:
    if c.isupper():
        count += 1

print(count)