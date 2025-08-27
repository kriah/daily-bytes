''' Acceptable String
Given a string, s, make it acceptable. An acceptable string is a string that contains no two 
adjacent characters that are the same with one letter being capitalized and the other being lowercased.
Note: An empty string is acceptable and only one distinct answer will exist.

Ex: Given the following string s…
s = "Aabb", return "bb".

Ex: Given the following string s…
s = "AabBcC", return "".
'''

s = "Aabb" # return "bb"
s = "AabBcC" # return ""

#s = "aabBcc" # return "aacc"
#s = "aabbcC" # return "aabb"

def clean_string(s):
    new_string = ''
    for i in range(len(s)-1):
        print(s[i], s[i+1])
        a = s[i] # current item
        b = s[i+1] # next item
        
        # checks if they are the same letter
        if (a.lower() == b.lower()):
            print("True")
            # check if one letter is uppercase and the other is lowercase
            if( (a.islower() and b.isupper()) or (a.isupper() and b.islower())):
                pass






print(clean_string(s))