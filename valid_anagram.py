''' Valid Anagram
Given two strings s and t return whether or not s is an anagram of t.
Note: An anagram is a word formed by reordering the letters of another word.

Ex: Given the following strings...

s = "cat", t = "tac", return true
s = "listen", t = "silent", return true
s = "program", t = "function", return false
'''

s = "listen"
t = "silent"
#s = "program"
#t = "function"


def compare_strings(str1, str2):

    # if both strings aren't the same length then they aren't anagrams
    if len(str1) != len(str2):
        return False
    
    # checks if each letter in str1 is in str2
    for letter in str1:
        if letter not in str2:
            return False
    
    return True

print(compare_strings(s, t))