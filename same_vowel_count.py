''' Same Vowel Count
Given an even length string, s, return whether or not the first half of s and the second half of s contain the same number of vowels.

Ex: s = "laptop", return true (there is one vowel in "lap" and one vowel in "top").
Ex: s = "computer", return false.
'''

s = "laptop"
# s = "computer"

def vowel_count(s):
    middle = len(s)//2
    vowel = 'aeiou'
    count1 = 0 # counter for first half
    count2 = 0 # counter for second half

    for i in range(middle):
        # count number of vowels from the first half
        if s[i] in vowel:
            count1+=1
        # count number of vowels from the second half
        if s[middle+i] in vowel:
            count2+=1

    
    if count1 == count2:
        return True
    else:
        return False

print(vowel_count(s))