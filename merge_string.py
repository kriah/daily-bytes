''' Merge String
Given two strings, s and t, merge the two strings together alternating characters starting with s.
Note: If one string is longer than the other, append the remaining characters of the longer string 
at the end of the merged string.

s = "abc", t = "def", return "adbecf".
'''

s = "abc"
t = "defgh"

def merge_string(s, t):
    new_string = ""
    while s != "" and t != "":
        # add first item from s and t to the new string
        new_string += s[0] + t[0]
        s = s[1:] # remove first item from string
        t = t[1:] # remove first item from string
    
    # add remaining string to new string
    new_string += s + t
    return new_string

print(merge_string(s, t))