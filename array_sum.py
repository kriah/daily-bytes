''' Array Sum
Given an integer array, nums, return an array containing its running sum at every index.

Ex: Given the following nums…
nums = [1, 2, 3], return [1, 3, 6].

Ex: Given the following nums…
nums = [10], return [10].
'''

nums = [1, 2, 3]
#nums = [10]
sums = [] # contains running sum at every index
current_sum = 0 # running sum at current index

for i in nums:
    current_sum += i
    sums.append(current_sum)

print(sums)