# Reading and Praying
# 7/13/17
# CTI-110 M6HW2 - Random Number File Reader
# Shawn Trusdell
#
import random

def main():
        more = 'y'

        while more.lower() == 'y':

                random_numbers = open('Random.txt', 'w')
                NumtoBeWr = random.randint(1, 10)
                print(NumtoBeWr, 'numbers added to output file: ')

                for count in range(NumtoBeWr):
                      number = random.randint(1, 500)
                      print(number)
                      random_numbers.write(str(number) + '\n')

                random_numbers.close()

                random_numbers = open('Random.txt', 'r')

                line = random_numbers.readline()
                number = 0
                total = 0

                while line:
                   number += int(line)
                   total += 1
                   line = random_numbers.readline().rstrip("\n")
                   print("Total: " + str(total))
                   print("Total amount of numbers read: " + str(number))
                   more = input("Do you wish to run again? (Y/N): ")
                random_numbers.close()
main()
