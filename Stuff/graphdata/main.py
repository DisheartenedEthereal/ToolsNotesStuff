#!/usr/bin/env python
import os,sys
#
# DEFINES
#
def clr():
    os.system("clear")


def takeinp():
    try :
        ret = int(input("~> "))
        return ret
    except ValueError:
        print("Only Numbers allower")
        takeinp()
def giveoption(text,num):
    print("["+str(num)+"]"+" - " +text)

#
# MAIN
#
if __name__ == '__main__':
    clr()

    giveoption("Help",0)
    giveoption("Pings",1)
    giveoption("Pings-from",2)
    giveoption("Ram",4)
    giveoption("Cpu",5)
    giveoption("Status",6)
    giveoption("Runcommand",7)
    option = takeinp()

    if option == 0:
        print("Hello, its self explanatory.")
    elif option == 1 :
        #checkforpings()
        #graphpings()
        pass
    else :
        option = takeinp()


