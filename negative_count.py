""" Negative Count
Given an MxN matrix, which is sorted in decreasing order (row-wise and column-wise), return the total number of negative values in the array.

Ex: Given the following matrix…
matrix = [
  [3, -1],
  [2, -2]
], return 2 (-1 and -2 are negative).

Ex: Given the following matrix…
matrix = [
  [4, 3],
  [2, 1]
], return 0.
"""


matrix = [
  [3, -1],
  [2, -2]
]

sum = 0

# Iterate through matrix to find negative numbers
for row in matrix:
  for item in row:
    if item < 0:
      sum += 1

print("There are", sum, "negative numbers in the matrix.")
