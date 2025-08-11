''' Eating Candy
You are given a certain number of candies and an exchange rate. For every exchange number of candy wrappers that you trade in, you receive an additional candy. Return the maximum number of candies that you can eat.
Note: Each candy is wrapped in a candy wrapped.

Ex: Given the following candies and exchange…

candies = 3, exchange = 3, return 4 (each your three candies, exchange 3 wrappers, each additional candy).
Ex: Given the following candies and exchange…

candies = 3, exchange = 4, return 3.
'''

candies = 6
exchange = 3

def candy_exchange(candies, exchangeRate):
    return candies + candies//exchangeRate


print(candy_exchange(candies, exchange))
