import time,sys
import os

def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  
def typingInput(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  value = input()  
  return value
def get_platform():
    pl = sys.platform
    if pl == "linux" or pl == "linux2":
        return "linux"
    elif pl == "darwin":
        pass
    elif pl == "win32":
        return "windows"
    else :
        return "UNSUPP"
def osdecider(lin,win):
    if get_platform() == "linux":
        os.system(lin)
    elif get_platform() == "windows":
        os.system(win)
    else:
        print("UNSUPP, exiting.")
def shittyborder(text,spc):
    osdecider("clear","cls")
    columns, rows = os.get_terminal_size(0)
    print(text*columns)
    for i in range(spc):
        print("\n")
def termC():

    
    columns, rows = os.get_terminal_size(0)
    return columns
def termR():

    columns, rows = os.get_terminal_size(0)
    return rows
import time
def countdown(p,q):
    i=p
    j=q
    k=0
    while True:
        if(j==-1):
            j=59
            i -=1
        if(j > 9):  
            print(str(k)+str(i)+":"+str(j), end="\r")
        else:
            print(str(k)+str(i)+":"+str(k)+str(j), end="\r")
        time.sleep(1)
        j -= 1
        if(i==0 and j==-1):
            break
    if(i==0 and j==-1):
        print("Time was not on your side!", end="\r")
        time.sleep(1)

