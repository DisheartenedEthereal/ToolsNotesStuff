import sys,os
def parse(cmd):
    os.system(cmd)
def prompt():
    v = input("- HADEN :  ")

    return v
try:
    c = prompt()
    if c != "exit":
        parse(c)
    else:
        sys.exit()
except KeyboardInterrupt:
    print("\n")
    c = prompt()
    if c != "exit":
        parse(c)
    else:
        sys.exit()
