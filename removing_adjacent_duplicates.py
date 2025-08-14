''' Removing Adjacent Duplicates
Given a string s containing only lowercase letters, continuously remove adjacent characters that are the same and return the result.

Ex: Given the following strings...

s = "abccba", return ""
s = "foobar", return "fbar"
s = "abccbefggfe", return "a"
'''

s = "abccba"
s1 = "foobar"
s2 = "abccbefggfe"

def remove_duplicates(s):
    index = 0
    new_string = ""

    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            s1 = s[:i] + s[i+2:]
            print("s1:", s1)
            remove_duplicates(s1)
        else:
            continue 


print(remove_duplicates(s2))