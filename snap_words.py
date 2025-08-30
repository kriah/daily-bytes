''' Snap Words
Given a string s, reverse the words.
Note: You may assume that there are no leading or trailing whitespaces and each word within s is only separated by a single whitespace.

Ex: Given the following string s…
s = "The Daily Byte", return "Byte Daily The".
'''

s = "The Daily Byte"
split_string = s.split(" ") # split string
split_string = split_string[::-1] # reverses order of list
new_string = " ".join(split_string) # rejoin words from list to string
print(new_string)
