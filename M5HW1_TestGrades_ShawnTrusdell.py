# Calculating Test Grades
# 2 JULY 2017
# CTI-110 M5HW1 - Test Average and Grade
# SHAWN TRUSDELL
#
max=5
total=0.0
print('Please enter',max,'test scores')
for counter in range (max):
    test=int(input('Score? '))
    total= test + total
    if test <= 100 and test >= 90:
        print('A')
    if test <= 89 and test >= 80:
        print('B')
    if test <= 79 and test >= 70:
        print('C')
    if test <= 69 and test >= 60:
        print('D')
    if test < 60:
        print('F')
calc_average= total / max
print('Your average is',calc_average)
