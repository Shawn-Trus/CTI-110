# ADDING SUMS
# JUNE 25 2017
# CTI-110 M4HW1 - Sum of Numbers
# Shawn Trusdell
#
total= 0.0
print('This program will get the sum of your numbers.')
number = int(input('What number would you like to add: '))
while number > 0:
    total= number + total
    number = int(input('What number would you like to add: '))
    if number < 0:
        print('Sorry cannot not input negative numbers.')
print('Your total is: ',total)
