''' One Fourth
Given an array of integers, nums, sorted in ascending order, return the element that occurs 
more than one fourth of the time.
Note: If no element appears more than a fourth of the time, return -1.

Ex: Given the following nums…

nums = [1, 2, 2, 3, 4], return 2.
Ex: Given the following nums…

nums = [1, 2, 3, 4], return -1.
'''

nums = [1, 2, 3, 4]
nums1 = [1, 2, 2, 3, 4]
nums2 = [1, 1, 1, 3, 4, 1, 2, 2]

def one_fourth(nums):
    unique_values = set(nums) # set of uniques number from nums
    min = len(nums) / 4 # value of 1/4 of the array
    fourth = -1

    for num in unique_values:
        num_count = nums.count(num)
        if num_count > min and num_count > nums.count(fourth):
            fourth = num

    return fourth
    

print(one_fourth(nums))