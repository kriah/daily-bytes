''' Rearrange Elements
Given an array of numbers, move all zeroes in the array to the end while maintaining 
the relative order of the other numbers.
Note: You must modify the array you’re given (i.e. you cannot create a new array).

Ex: Given the following array nums…
nums = [3, 7, 0, 5, 0, 2], rearrange nums to look like the following [3,7,5,2,0,0]
'''

nums = [3, 7, 0, 5, 0, 2]
#nums = [3, 7, 0, 0, 0, 2]

def rearrange(nums):
    index = 0 # index in array
    count_zeros = nums.count(0) # counts number of zeros

    while (index < len(nums) - count_zeros):
        # checks if value at index is 0
        if nums[index] == 0:
            nums = nums[:index] + nums[index+1:] # remove 0 from the array
            nums.append(0) # adds 0 to the end of the array
        else:
            index += 1 # goes to the next index if value not 0
    
    return nums

    
print(rearrange(nums)) 