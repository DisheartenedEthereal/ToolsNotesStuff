#!/usr/bin/env python
# Imports
import os
import datetime
rows, columns = os.popen('stty size', 'r').read().split()


def banner():
    """This is the banner"""
    os.system("clear")
    banner = open("banner.txt")
    text = banner.read()
    print(text)
    print("-"*int(columns))


def startop():
    """This is the normal operation for running start,
    includes logging and stuff"""
    print("Start time : " + datetime.datetime.now())


def stopop():
    pass


def option(num, title):
    print("    ["+str(num)+"] - "+str(title))


def functiondecider(TAKE):

    if TAKE == 99:
        print("Exiting cleanly...")
    elif TAKE == 0:
        pass   # do ip menu
    elif TAKE == 1:
        startop()
    elif TAKE == 2:
        stopop()


def menu():
    allowed = [0, 1, 2, 99]
    option(0, "Go to monitor")
    option(1, "Stop service")
    option(2, "Start service")
    option(99, "Exit")
    try:
        take = int(input("ANONTOOLS# "))
    except ValueError:
        take = int(input("ANONTOOLS# "))
    if (take in allowed) is True:
        functiondecider(take)
    else:
        print("INVALID OPTION")
        take = int(input("ANONTOOLS# "))


if __name__ == "__main__":
    banner()
    menu()
