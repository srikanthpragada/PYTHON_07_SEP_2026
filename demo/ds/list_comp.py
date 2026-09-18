l  = ['10', '20', '30', '5']

nums = []
for e in l:
    nums.append(int(e))
print(sum(nums))

# List Comprehension
nums = [int(e) for e in l]

print(sum(nums))
