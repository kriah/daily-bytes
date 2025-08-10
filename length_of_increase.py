''' Length of Increase
Given an integer array, nums, return the length of the longest increasing subarray.
Note: The subarray must be strictly increasing.

Ex: Given the following nums.
nums = [1, 2, 3], return 3.

Ex: Given the following nums.
nums = [3, 4, 1, 2, 8], return 3.
'''

nums = [3, 4, 5, 2, 8] #[1, 2, 3, 4, 8]
nums = [1, 2, 6, 7, 8]

def increasing_interval(nums):
    nums.sort()

    count = 0

    print(nums)


increasing_interval(nums)