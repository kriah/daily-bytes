''' Find Bunches
Given a string S that contains only lowercase letters, return a list containing the intervals of all the bunches. 
A bunch is a set of contiguous characters (larger than two) that are all the same. An interval that represents a 
bunch contains the starting index of the bunch and the ending index of the bunch.
Note: The intervals returned should be in ascending order according to start indexes.

Ex: Given the following string S...
S = “aaabbbccc”, return [[0,2],[3,5],[6,8]].

Ex: Given the following string S...
S = “aaabbcddddd”, return [[0,2],[6,10]].
'''

s1 = 'aaabbbccc' # [[0,2], [3,5], [6,8]]
s2 = 'aaabbcddddd' # [[0,2], [6,10]]

def find_intervals(s):
    letter = s[0]
    start = 0
    intervals = []

    for i in range(len(s)):
        if i == len(s)-1:
            intervals.append([start,i])
        elif s[i] == letter:
            print(letter)
        else:
            letter = s[i]
            intervals.append([start,i-1])
            start = i

    return intervals


print(find_intervals(s1))