#!/usr/bin/env python 
import os,sys,time
path_to_pic = ""
path_to_vid = ""
config_memorylimit = int(1000000)
def check():
    free_mem_in_kb = 0
    with open('/proc/meminfo') as file:
        for line in file:
            if 'MemFree' in line:
                free_mem_in_kb = line.split()[1]
                break
    if int(free_mem_in_kb) >= config_memorylimit:
        return 0
        
    else:
        return 1
while True:
    if check() == 0:
        print(str(time.time())+ "Pass")
    else:
        print(str(time.time())+ "Fail")
    time.sleep(10)
