def count_positive(nums):
    count = 0
    for n in nums:
        if n > 0:
            count += 1

    return count

print(count_positive( [-10, 9, 8, 0, -3]))
