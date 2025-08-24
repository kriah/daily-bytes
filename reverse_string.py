''' Reverse String
Given a string, reverse all of its characters and return the resulting string.

Ex: Given the following strings...

“Cat”, return “taC”
“The Daily Byte”, return "etyB yliaD ehT”
“civic”, return “civic”
'''

str1 = "The Daily Byte"
new_string = ""

for char in str1:
    new_string = char + new_string
    
print(new_string)


