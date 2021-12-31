# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
#!/usr/bin/python3
import argparse
import os
import sys
import time
import subprocess
import socket
import click
import getopt 
os.system("clear")
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# %%

## def page
def clean():
    os.system("clear")
def OsDir(cmd):
    os.chdir("/home/disheartenedethereal")
    os.system(cmd)
def exit():
    sys.exit()
def killmethod_shadowsocks():
    OsDir("killall ss-local")
def runmethod_shadowsocks():
    OsDir("ss-local -c ss-config.json &")
def killmethod_tor():
    OsDir("killall tor &")
def runmethod_tor():
    OsDir("killall tor &")
    time.sleep(2)
    OsDir("tor &")
def checkip(proxy,port):
    if proxy == "socks5":
        # return OsDir("curl --socks5 127.0.0.1:"+port+ " ifconfig.me")
        os.system("curl -s --socks5 127.0.0.1:"+port+ " ifconfig.me > tmp"+port)
        return open('tmp'+port, 'r').read()
    else :
        print("CHECKIP_ERROR")
def killproxies(name):
    
    if name == "tor":
        killmethod_tor()
    elif name == "ss":
        killmethod_shadowsocks()
    elif name == "all":
        killmethod_shadowsocks()
        killmethod_tor()
    else:
        print("\nNo proxy selected, exiting...")
        exit()
def parse():

    parser = argparse.ArgumentParser()
    parser.add_argument('-k', '--kill', help="Choose what to kill: ss|tor", metavar="")
    parser.add_argument('-r', '--run', help="Choose what to run: ss|tor", metavar="")
    args = parser.parse_args()
    # ... do something with args.output ...
    # ... do something with args.verbose ..
    
    if args.kill == "ss" or args.kill == "shadowsocks" or args.kill == "shadow":
        killmethod_shadowsocks()
    elif args.kill == "tor":
            killmethod_tor()
            print("killed tor")
    if args.run == "ss":
        runmethod_shadowsocks()


# %%
def main():
    try: 
        
        f = open("banner.txt", "r")
        print("\n")
        print(f.read())
        print("\n")
        f.close()
        killswitch = input("\nShould we kill all existing connections? Y/N : ")
        if killswitch == "Y" or killswitch == "y" or killswitch == "yes":
            killproxies("all")
            print()
        elif killswitch == "N" or killswitch == "n" or killswitch == "no":
            def killmenu():
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                tor_res = sock.connect_ex(('127.0.0.1',9050))
                if tor_res == 0 :
                    TOR_status = bcolors.OKGREEN + "ACTIVE: "+ checkip("socks5","9050") + bcolors.ENDC
                else :
                    TOR_status = bcolors.WARNING + "OFFLINE" + bcolors.ENDC
                tor_web = sock.connect_ex(('127.0.0.1',9150))
                if tor_web == 0 :
                    TORRES_status = bcolors.OKGREEN + "ACTIVE: " + checkip("socks5","9150") + bcolors.ENDC
                else :
                    TORRES_status = bcolors.WARNING + "OFFLINE" + bcolors.ENDC
                ss_1 = sock.connect_ex(('127.0.0.1',1080))
                if ss_1 == 0 :
                    SS_status = bcolors.OKGREEN + "ACTIVE: " + checkip("socks5","1080") + bcolors.ENDC
                else :
                    SS_status = bcolors.WARNING + "OFFLINE" + bcolors.ENDC
                ss_2 = sock.connect_ex(('127.0.0.1',1081))
                if ss_2 == 0 :
                    SS2_status = bcolors.OKGREEN + "ACTIVE: " + checkip("socks5","1081")+ bcolors.ENDC
                else :
                    SS2_status = bcolors.WARNING + "OFFLINE" + bcolors.ENDC
                sock.close()
                print("\n")
                print("-"*25)
                print(" 1- Tor: " + TORRES_status+"\n 2- Tor Browser: "+TORRES_status+"\n 3- ShadowSocks 1: "+SS_status+"\n 4- Shadowsocks 2: "+SS2_status)
                print("-"*25)
                print("\n")
                step2 = input("\nSelect from the list above or NONE : ")
                killproxies(step2)
                exit()
            killmenu()
        else:
            exit()
    except KeyboardInterrupt:
        print("\nInterrupetd via CTRL C, exiting cleanly.")
        exit()
    except MemoryError:
        print("\nMemory ran out, exiting cleanly.")
        exit()


# %%


## main

#enabled_proxy = 0
def Argv():
    if len(sys.argv) == 1 :
        main()
    else:
        parse()
    


    
Argv()


# %%



