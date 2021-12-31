import os,sys
os.system("rm -rf isolation")
os.system("mkdir isolation && mkdir isolation/C: && mkdir isolation/C:/System && mkdir isolation/C:/User && mkdir isolation/C:/User/Documents && mkdir isolation/C:/User/Pictures")
for i in range(255):
    os.system("touch isolation/C:/System/System"+str(i))

for i in range(30):
    os.system("touch isolation/C:/User/Documents/Doc"+str(i))
for i in range(255):
    os.system("cp samplepic.png isolation/C:/User/Pictures/Pic"+str(i)+".png")