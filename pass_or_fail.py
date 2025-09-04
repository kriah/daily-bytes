''' Pass or Fail
You are given a string, attendance that represents a student’s class attendance throughout the semester. 
A student can be marked, A for absent, L, for late, or P for present. To get credit for the class, a 
student cannot miss more than one class and cannot come late to class twice in a row. Given the current 
students attendance record, return whether or not the student has passed the class.

Ex: Given the following attendance of a student… 
attendance = "PLPAPPPA", return false.

Ex: Given the following attendance of a student…
attendance = "PLPLPLPALP", return true.
'''

attendance = "PLPAPPPA" # return false.
attendance = "PLPLPLPALP" # return true.

def class_credit(attendance):
    # Checks for > 1 absence or two lates in a row
    if(attendance.count('A') > 1 or 'LL' in attendance):
        return False
    return True

print(class_credit(attendance))

