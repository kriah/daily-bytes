''' Valid Palindrome
Given a string, return whether or not it forms a palindrome ignoring case and non-alphabetical characters.
Note: a palindrome is a sequence of characters that reads the same forwards and backwards.

Ex: Given the following strings...

"level", return true
"algorithm", return false
"A man, a plan, a canal: Panama.", return true
'''

str1 = "level"
str2 = "algorithm"
str3 = "A man, a plan, a canal: Panama."

def is_palindrome(str1):
    reverse = -1
    for i in range(len(str1)):
        print('s:', str1[i], 't:', str1[reverse])
        if not str1[i].isalpha():
            print('Yes')
        elif not str1[reverse].isalpha():
            print('No')
        elif str1[i] != str1[reverse]:
            return False
        reverse -= 1

    return True

print(is_palindrome(str3))