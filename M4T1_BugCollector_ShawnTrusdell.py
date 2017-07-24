# Keeping a running total
# June 25 2017
# CTI-110 M4T1 - Bug Collector
# Shawn Trusdell
#
max = 5
total = 0.0
print('This program will add the number of bugs you have collected within')
print(max,'days')
for counter in range(max):
      number = float(input('How many bugs do you have today? '))
      total = total + number
print('Your total is')
print(total, 'bugs')
