''' One Fourth
Given an array of integers, nums, sorted in ascending order, return the element that occurs 
more than one fourth of the time.
Note: If no element appears more than a fourth of the time, return -1.

Ex: Given the following nums…

nums = [1, 2, 2, 3, 4], return 2.
Ex: Given the following nums…

nums = [1, 2, 3, 4], return -1.
'''

nums = [1, 2, 2, 3, 4]
nums2 = [1, 1, 1, 3, 4, 1, 2, 2]

def oneFourth(nums):
    uniqueValues = set(nums)
    length = len(uniqueValues)
    min = length / 4
    fourth = 0

    for num in uniqueValues:
        if nums.count(num) > min:
            fourth = num

    return fourth
    

print(oneFourth(nums2))