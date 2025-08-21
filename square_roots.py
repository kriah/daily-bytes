''' Square Roots
Given a non-negative integer x, return its square root.
Note: You may not use a built in square root function and decimals should be truncated to return an integer value.

Ex: Given the following x...
x = 9, return 3.

Ex: Given the following x...
x = 12, return 3.
'''

x = 12

def square_root(x):
    return int(x**0.5)


print(square_root(x))