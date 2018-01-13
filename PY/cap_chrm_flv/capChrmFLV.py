#!/usr/bin/python3

import time
import os
import sys
import shutil

import re

CaptureFrom = 'C:\\Users\\jerry.xie\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Pepper Data\\Shockwave Flash'
            # "C:/Users/jerry.xie/AppData/Local/Google/Chrome/User Data/Default/Pepper Data/Shockwave Flash"
CaptureTo = 'c:\\media\\temp'
            # "c:/media/temp"

def CapChromeFLV(targetName=""):

    try:
        if (not os.path.exists(CaptureFrom)) \
                or (not os.path.isdir(CaptureFrom)):
            print("Capture path not exist or not a directory: ", CaptureFrom)
            return
    except Exception as e:
        print(e)

    os.chdir(CaptureFrom)

    try:
        #print("Check capture-to path: ", CaptureTo)
        os.makedirs(CaptureTo, exist_ok=True)
    except Exception as e:
        print(e)

    print("Check Chrome Cache.")
    print("From: ", CaptureFrom)
    print("To:   ", CaptureTo)
    print("-"*50)
    print("  From  \t->  To")

    i = 0
    while True:
        for f in os.listdir(CaptureFrom):
            if f.endswith(".tmp"):
                fromf = CaptureFrom + "\\" + f
                tof = CaptureTo + "\\" + f
                if os.path.isfile(tof):                                       # same filename exist in capture-to-dir
                    if os.stat(tof).st_size == os.stat(fromf).st_size:        # same size, bypass
                        continue
                shutil.copyfile(fromf, tof)
                print(f, "\t->  ", f)          #print(fromf," -> ", tof)

        time.sleep(1)
        i += 1
        if (i >= 300):
            break



if __name__ == "__main__":
    CapChromeFLV()