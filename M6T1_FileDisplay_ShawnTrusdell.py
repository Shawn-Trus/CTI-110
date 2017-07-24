# Display numbers.txt
# 7/11/17
# CTI-110 M5T1 - File Display
# Shawn Trusdell
myfile = open('numbers.txt', 'r')
for line in myfile:
	number = int(line)
	print(number)
myfile.close()
