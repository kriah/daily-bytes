''' Sum Unique Elements
Given an array of integers, nums, return the sum of all uniquely occurring elements.

Ex: nums = [1, 3, 5, 5, 2], return 6 (1 + 3 + 2).
Ex: nums = [4, 4, 2, 3, 3, 2], return 0.
'''

nums = [1, 3, 5, 5, 2]

def sum_elements(nums):
    sum = 0

    for item in nums:
        if nums.count(item) == 1:
            sum += item
    
    return sum

print(sum_elements(nums))