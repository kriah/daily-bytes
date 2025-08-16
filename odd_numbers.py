''' Odd Numbers
Given two non-negative integers low and high, return the total count of odd numbers between them (inclusive).

Ex: Given the following low and high…

low = 1, high = 3, return 2 (1 and 3 are both odd).
Ex: Given the following low and high…

low = 1, high = 10, return 5.
'''

low = 1
high = 10
count = 0

# Iterate through range to find all odd numbers
for num in range(low, high+1):
  if num%2 == 1:
    count += 1

print("There are", count, "odd numbers between", low, "and", high, ".")
