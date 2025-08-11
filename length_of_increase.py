''' Length of Increase
Given an integer array, nums, return the length of the longest increasing subarray.
Note: The subarray must be strictly increasing.

Ex: Given the following nums.
nums = [1, 2, 3], return 3.

Ex: Given the following nums.
nums = [3, 4, 1, 2, 8], return 3.
'''

nums = [1, 2, 3]
nums1 = [3, 4, 1, 2, 8]
nums2 = [3, 4, 5, 2, 8]

def increasing_interval(nums):
    count = 1
    current_count = 0

    for i in range(len(nums)-1):
        if (nums[i] < nums[i+1]):
            count += 1
        else:
            if (count > current_count): 
                current_count = count
            count = 1

    return current_count

print("Count:", increasing_interval(nums2))