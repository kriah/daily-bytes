''' Word Length
Given a string, s, return the length of the last word.
Note: You may not use any sort of split() method.

Ex: Given the following string…
s = "The Daily Byte", return 4 (because "Byte" is four characters long).
'''

s = "The Daily Byte"

def count_last_word(s):
    index = len(s)-1 # start with the last character

    while index > 0:
        # if the char is a space then the chars to the right are the last word
        if (s[index] == " "):
            return len(s[index+1:]) # return the length of last word
        index -= 1

    return len(s) #otherwise length if it's one word

print(count_last_word(s))