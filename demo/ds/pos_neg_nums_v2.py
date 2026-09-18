# Take numbers until 0 and display pos first and then negative
pos_nums = []
neg_nums = []

while True:
    n = int(input("Enter a number [0 to stop] :"))
    if n == 0:
        break
    if n > 0:
        pos_nums.append(n)
    else:
        neg_nums.append(n)

print(pos_nums + neg_nums)


# # Print positive numbers
# for n in pos_nums:
#     print(n)
#
# # Print negative numbers
# for n in neg_nums:
#     print(n)
