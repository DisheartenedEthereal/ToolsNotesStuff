import os,sys,time

print("Starting tor-1")
os.system("tor -f rc-1 > rc1.log & tor -f rc-2 > rc2.log & tor -f rc-3 > rc3.log&")
time.sleep(15)
print("Tor-1 ip :")
os.system("torsocks -P 9297 curl ifconfig.me")
print("\nTor-2 ip :")
os.system("torsocks -P 9299 curl ifconfig.me")
print("\nTor-3 ip :")
os.system("torsocks -P 9300 curl ifconfig.me")
