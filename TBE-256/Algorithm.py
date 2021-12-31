# Lets do the imports first
import time
import os
import sys
import string
import math
import sys
# Some variables to declare first
STime = time.time()
AllASCII = list(str(string.printable))
AllASCII.append('')

# Decoder system (ye ye ik its really dumb but it works)

def HexaArea(s):
    return ((3 * math.sqrt(3)* (s*s)) / 2)
def generateKey(Time):
    ttime = str(Time)
    newstr = ttime.replace(".", "")
    Ntime = int(newstr)
    Hexa = int(HexaArea(Ntime))
    return Hexa

def keyToAscii(encoded,key):
    # we get encoded text as string, lets remove the spacers that are -NOX-
    NoSpace = str(encoded.split("-NOX-"))
    # we need to generate the keycode based on the key given
    Gen = str(generateKey(key))
    # now we encrypt all ASCII characters with said key to compare them
    EncList = [str(AllASCII.index(x) * Gen) for x in AllASCII]
    # now we compare said lists to get the index number of matching characters
    pList = list(set(Gen).intersection(EncList))
    print(pList)

class TBE:
    def __init__(self,string):
        self.string = string
    def encrypt(self,string):
        print("-"*50)
        print("Key: " + str(generateKey(STime)))
        print("-"*50)
        k = open("key",'w')
        k.write(str(generateKey(STime)))
        k.close()
        plain = list(string)
        print("\n")

        encrypted_list = plain
        for x in plain:
            for y in AllASCII:
                if x == y :
                    encrypted_list[encrypted_list.index(x)] = str(AllASCII.index(y) * generateKey(STime)) + "-NOX-"
                    break
        o = open("temp.enc",'w')
        o.write(''.join(encrypted_list))
        o.close()
        return ''.join(encrypted_list)
        
    def decrypt(self, string,key):
        string1 = open(string,'r')
        key1 = open(key,'r')
        string1.close
        key1.close
        return keyToAscii(str(string1.read()),str(key1.read()))

test1 = TBE("In publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content. Lorem ipsum may be used as a placeholder before final copy is available.")
# print(test1.encrypt(test1.string))

print(test1.decrypt("temp.enc","key"))

# f = open('C_classes.zip', 'rb')
# file_content = str(f.read())
# print(len(file_content))
# file1 = TBE(file_content)

# # 1614959666.6055105

# f.close()


# d = open('c.enc','w')
# d.write(file1.encrypt(file1.string))
# d.close()