# Finding the Areas
# 14 JUNE 2017	
# CTI-110 M3T1 - Areas of Rectangles
# SHAWN TRUSDELL
#

Width1= int(input('Input the Width of the 1st Rectangle: '))
Length1= int(input('Input the Length of the 1st Rectangle: '))
Width2= int(input('Input the Width of the 2nd Rectangle: '))
Length2= int(input('Input the Length of the 2nd Rectangle: '))
Rectangle1= Width1 * Length1
Rectangle2= Width2 * Length2
if Rectangle1 > Rectangle2:
	print ('The First Rectangle is Greater!')
	print (Rectangle1)
	
if Rectangle1 < Rectangle2:
        print ('The Second Rectangle is Greater!')
        print (Rectangle2)
        
if Rectangle1 == Rectangle2:
        print ('These Rectangles are Congruent')
        print (Rectangle1, Rectangle2)
        
