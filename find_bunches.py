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

s1 = 'aaabbbcccdd' # [[0,2], [3,5], [6,8]]
s2 = 'aaabbcdddddee' # [[0,2], [6,10]]

def find_intervals(s):
    count = 0 # counter to track number of letters
    start = 0 # index of the start of interval
    letter = s[0]
    intervals = [] # will contain the intervals
    
    # iterate through array to find intervals
    for i in range(len(s)):
        
        if s[i] == letter:
            count += 1 # increase count by 1
            
            # if item is the last element in array and there's
            # more than 2 of the same letter then append interval
            if i == len(s)-1 and count > 2:
                intervals.append([start,i])
        else:
            if count > 2:
                intervals.append([start,i-1])
            letter = s[i] # update next letter
            start = i # update start of next interval
            count = 1 # reset count

    return intervals

print(find_intervals(s1))
print(find_intervals(s2))