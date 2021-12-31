#!/usr/bin/env python3
# Path: emtehan.py
import sys
PASSWORD = "PASS"
def getPass(passfail = False):
    if passfail == False:
        return input("Enter your password: ")
    return input("Retry, Enter your password: ")
class inp:
    def __init__(self):
        self.n_of_tries = 0
        try:
            while True:
                p = ""
                if self.n_of_tries != 0:
                    p = getPass(True)
                    if p == PASSWORD:
                        break
                else:
                    p = getPass()
                    self.n_of_tries += 1            
                    if p == PASSWORD:
                        break
            self.getArray()
            self.popFromArray()
            print("Operation complete, array = ", self.array)
        except KeyboardInterrupt:
            print("\nExiting safely.")
    def getArray(self):
        try:
            arr = input("Enter array (only integers allowed, seperate with a whitespace): ").split(' '); self.array = list(map(int,arr))
        except:
            print("Not enough items in array.")
        try:
            if (len(self.array) < 4):
                self.array = []
                print("Invalid input, try again, input needs to be at least 4, exiting.") ; sys.exit()
        except AttributeError:
            print("Array cannot have trailing whitespace, double whitespace, or be a string, exiting.") ; sys.exit()
    def popFromArray(self):
        try:
            n = int(input("Enter index: ")); x = self.array[:n];
        except ValueError:
            print("Index must be a number") ; sys.exit()
        try:
            for i in range(n):
                self.array.pop(0)
        except:
            print("Value bigger than list itself, exiting."); sys.exit()
        for i in x:
            self.array.append(i)
obj = inp()