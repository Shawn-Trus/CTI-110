# Random File Writer
# 7/13/17
# CTI-110 M6HW1 - Random Number File Writer
# Shawn Trusdell
#
import random
afile = open('Random.txt', 'w')
for i in range(int(input('Please specify how many? '))):
	line = str(random.randint(1,500))
	afile.write(line)
	print(line)
afile.close()
