''' Length of Increase
Given an integer array, nums, return the length of the longest increasing subarray.
Note: The subarray must be strictly increasing.

Ex: Given the following nums.
nums = [1, 2, 3], return 3.

Ex: Given the following nums.
nums = [3, 4, 1, 2, 8], return 3.
'''

nums = [1, 2, 3] #returns 3
nums1 = [3, 4, 1, 2, 8] # returns 3
nums2 = [3, 4, 5, 2, 8] # returns 3
nums3 = [5, 4, 3, 2, 1] # returns 1

def increasing_interval(nums):
    count = 1
    current_count = 1

    # iterate through the list up until the last item
    for i in range(len(nums)-1):
        # checks if the current item is less than the next item
        if (nums[i] < nums[i+1]):
            count += 1
        else:
            count = 1 # reset count if next item is smaller
        
        # assign the largest interval to current_count
        if (count > current_count): 
                current_count = count

    return current_count

print("Count:", increasing_interval(nums))
print("Count:", increasing_interval(nums1))
print("Count:", increasing_interval(nums2))
print("Count:", increasing_interval(nums3))