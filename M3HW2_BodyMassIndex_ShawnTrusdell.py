# BMI
# 17 JUNE 2017	
# CTI-110 M3HW2 - Body Mass Index
# Shawn Trusdell
#
Weight= float(input('How much do you weigh? '))
Height= float(input('How tall are you in inches? '))
BMI = Weight * 703/(Height * Height)
print ('Your BMI is ',BMI)
if BMI <= 18.5:
	print ('You seem to be alittle underweight.')
if BMI >= 18.5 and BMI <= 25:
	print ('You are in great shape!')
if BMI > 25:
	print ('You seem to be alittle overweight')
