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
    new_string = str1.lower()
    txt = [',', ':', '.', " "]
    for item in txt:
        new_string = new_string.replace(item, "")

    reverse = -1
    for i in range(len(new_string)):
        if new_string[i] != new_string[reverse]:
            return False
        reverse -= 1
    return True

print(is_palindrome(str1)) # True
print(is_palindrome(str2)) # False  
print(is_palindrome(str3)) # True 