def ispositive(n):
    #print('Testing', n)
    return n > 0


nums = [-10, 0, 3, 5, 10, -9]

for v in filter(ispositive, nums):
    print(v)


