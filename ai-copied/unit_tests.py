import requests
import sys
import os, subprocess

# Globals / config
URL = "127.0.0.1:9292"
class test(object):
    """Class for initiliazing tests"""
    def __init__(self, name, type, exp, desc, adr = False):
        super(test, self).__init__()
        self.adr = adr
        self.exp = exp
        self.name = name
        self.type = type
        self.desc = desc
    def doTUI(self):
        print("[*] Test : ", self.name, ",Expected :", self.exp)
    def checkResults(self,res):
        if res == self.exp:
            return True
        else:
            return False
    def doResults(self,result):
        if result == True:
            print("- Passed.")
        else:
            print("- FAILED.")
    def doGET(self):
        if self.adr == False:
            sys.exit
        r = subprocess.check_output(["curl","-s", self.adr])
        return r.decode('UTF-8')
    def check(self):
        self.doTUI()
        if self.type == "GET":
            self.doResults(self.checkResults(self.doGET()))
t1 = test("Rackup / Basic rest answer","GET","Hello!","checks if rack is up","127.0.0.1:9292/hello")
t1.check()
