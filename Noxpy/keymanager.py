import os
import TBE as t
def delkey(path="key.hateme", passes=1):
    with open(path, "ba+") as delfile:
        length = delfile.tell()
        for i in range(passes):
            delfile.seek(0)
            delfile.write(os.urandom(length))
    os.remove(path)
def genkey():

    t.write_key()
def prkey():
    pass
