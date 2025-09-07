''' Reverse Vowels
Given a string, reverse the vowels of it.
Note: In this problem y is not considered a vowel.

Ex: s = "computer", return "cemputor"
Ex: s = "The Daily Byte", return "The Dialy Byte"
'''

s = "computer" # return "cemputor"
s = "The Daily Byte" # return "The Dialy Byte"

def reverse_vowels(s):
    vowels = 'aeiou'
    left_index = 0
    right_index = len(s)-1

    while(left_index < right_index):
        # if item from the left is not a vowel then move right to next item
        if(not s[left_index] in vowels):
            left_index += 1
        # if item from the right is not a vowel the move left to the next time
        elif(not s[right_index] in vowels):
            right_index -= 1
        # when both items are vowels
        else:
            # switch the value at the left index with the value at the right index
            new_string = s[:left_index] + s[right_index] + s[left_index+1: right_index] + s[left_index] + s[right_index+1:]
            s = new_string
            left_index += 1 # move to next item on the right
            right_index -= 1 # move the next item on the left

    return s

print(reverse_vowels(s))