# Function to count and print
# currency types
import sys
def countCurrency(amount):
     
    notes = [100000, 50000, 10000, 5000,
               2000, 1000, 500, 100, 50]
                
    noteCounter = [0, 0, 0, 0, 0,
                     0, 0, 0, 0]
     
    print ("Currency Count -> ")
     
    for i, j in zip(notes, noteCounter):
        if amount >= i:
            j = amount // i
            amount = amount - j * i
            print (i ," : ", j)
 
# main function
try:
    countCurrency(int(sys.argv[1]))
except IndexError:
    print("Usage : python main.py number")
