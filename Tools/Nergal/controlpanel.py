#!/usr/bin/python
import sys,os
def getTerminalSize():
    import os
    env = os.environ
    def ioctl_GWINSZ(fd):
        try:
            import fcntl, termios, struct, os
            cr = struct.unpack('hh', fcntl.ioctl(fd, termios.TIOCGWINSZ,'1234'))
        except:
            return
        return cr
    cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)
    if not cr:
        try:
            fd = os.open(os.ctermid(), os.O_RDONLY)
            cr = ioctl_GWINSZ(fd)
            os.close(fd)
        except:
            pass
    if not cr:
        cr = (env.get('LINES', 25), env.get('COLUMNS', 80))

        ### Use get(key[, default]) instead of a try/catch
        #try:
        #    cr = (env['LINES'], env['COLUMNS'])
        #except:
        #    cr = (25, 80)
    return int(cr[1]), int(cr[0])
(width, height) = getTerminalSize()
def banner():

    #(width, height) = getTerminalSize()
    f = open("assets/banner","r")
    print(f.read())
    f.close()
    print("-"*width)
    print("\n")
    #print("\n")
def clr():
    os.system("clear")


def takeinp():
    try :
        ret = int(input("~> "))
        return ret
    except ValueError:
        print("Only Numbers allowed")
        takeinp()
    except KeyboardInterrupt:
        sys.exit()
def giveoption(text,num):
    print("["+str(num)+"]"+" - " +text)
def parseOptions(SELECT):
    if SELECT == 0:
        #doWormMenu()
        pass
    elif SELECT == 1:
        #doStatsMenu
        pass
    elif SELECT == 2:
        os.system("./create_virtual_env")
        print("-"* width)
        mainMenu()
    elif SELECT == 3:
        os.system("./reset_env")
        print("-"*width)
        mainMenu()
    elif SELECT == 99:
        sys.exit()
    else :
        print("Invalid selection")
        mainMenu()
def mainMenu():

    giveoption("Worms",0)
    giveoption("Statisctics",1)
    giveoption("Create Enviroment",2)
    giveoption("Reset Enviroment",3)
    giveoption("Exit",99)
    parseOptions(takeinp())
if __name__ == "__main__":
    clr()
    banner()

    mainMenu()
