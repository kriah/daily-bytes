''' Removing Vowels
Given a string s remove all the vowels it contains and return the resulting string.
Note: In this problem y is not considered a vowel.

Ex: s = "aeiou", return ""
Ex: s = "byte", return "byt"
Ex: s = "xyz", return "xyz"
'''

s1 = "aeiou"
s2 = "byte" 
s3 = "xyz" 


def remove_vowels(s):
    vowels = 'aeiou'
    new_string = ''

    for letter in s:
        # if a letter isn't a vowel then add to new string
        if letter not in vowels:
            new_string += letter

    return new_string
        

print(remove_vowels(s1))
print(remove_vowels(s2))
print(remove_vowels(s3))