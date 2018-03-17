0# Shawn Trusdell
# 01/25/18
# CSC121-0001
# Converting Temperature

def main():
    mainMenu()
    #F to C {Fahrenheit (°F) minus 32, times 5/9}
    # C to F {Celsius (°C) times 9/5 plus 32}
def mainMenu():
    #Display Menu for user
    #Allow user to choose to convert C-F or F-C
    print("Conversion Menu")
    print("-"*27)
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")
    print("-"*27)
    getInput()
def getInput():
    #Get user input on which conversion they would like to perform
    choice = input("Which would you like to convert [1-2]? ")
    if choice==1:
        print("*"*32)
        print("You have picked Fahrenheit to Celsius")
        toFahrenheit()
    elif choice==2:
        print("*"*32)
        print("You have picked Celsius to Fahrenheit")
        toCelsius()
        
def toCelsius():
    #calculation of C to F
    Cel = 0
    Cel = int(input("Please input Degree in Celsius: "))
    C_ans = (int(9 / 5 * Cel + 32))
    print "Your answer is", C_ans ,"degrees Fahrenheit"
    MayRestart()
    
def toFahrenheit():
    #Calculation of F to C
    Fah = 0
    Fah = int(input("Please input Degree in Fahrenheit: "))
    F_ans = (int((Fah - 32)* 5/9))
    print "Your answer is", F_ans ,"degrees Celsius"
    MayRestart()

def MayRestart():
    #Gives user option to restart
    print("-"*45)
    print("Would you like to Convert another Temperature?")
    print("-"*45)
    print("1 = yes")
    print("2 = no")
    option = input()
    if option==1:
        print("Resetting program")
        print("."*90)
        main()
    elif option==2:
        print("Goodbye..")
    
    
main()


