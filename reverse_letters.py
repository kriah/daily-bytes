''' Reverse Letters
Given a string s, reverse all of its characters that are letters and return the resulting string.

Ex: s = "abc*d", return "dcb*a".
Ex: s = "Ab&e]a-Ta", return "aT&a]e-bA".
'''

s1 = "abc*a"
s2 = "Ab&e]a-Ta"

def reverse_letters(s):
    left_index = 0
    right_index = len(s)-1
    middle = len(s)//2

    while (left_index < middle):
        # if item isn't in the alphabet then go to next item
        if(not s[left_index].isalpha()):
            left_index += 1
        # if item isn't in the alphabet then go to next item
        elif(not s[right_index].isalpha()):
            right_index -= 1
        else: 
            # switch the values at the left and right index
            new_string = s[:left_index] + s[right_index] + s[left_index+1: right_index] + s[left_index] + s[right_index+1:]
            s = new_string
            left_index += 1 # go to the next item from the left
            right_index -= 1 # go to the next item from the right

    return s


print(reverse_letters(s1))
print(reverse_letters(s2))