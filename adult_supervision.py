''' Adult Supervision
You are given a MxN matrix and a value k. Every value in the matrix is a one which represents an adult and a zero which represents a child. For every row in the matrix, adults appear before children. A row that has more adults than another row is more strongly supervised. Return the k rows of matrix that have the least amount of supervision in ascending order.
Note: It is guaranteed no ties will occur for the number of adults in a row.

Ex: Given the following matrix and k...
matrix = [
  [1, 1, 0],
  [1, 0, 0],
  [0, 0, 0]
], k = 3, return [2, 1, 0] (row 2 has least adults followed by row 1 and row 0).

Ex: Given the following matrix and k...
matrix = [
  [1, 1, 1],
  [1, 1, 0],
  [1, 0, 0]
], k = 2, return [2, 1].
'''

matrix = [
  [1, 1, 0],
  [1, 0, 0],
  [0, 0, 0]
]
k = 3


count = 0
for row in range(0, len(matrix)):
    count = 0
    print("Row:", row)
    for item in matrix[row]:
      if item == 1:
        count += 1
    print(count)
