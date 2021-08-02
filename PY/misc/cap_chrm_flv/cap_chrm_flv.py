#!/usr/bin/python3

import time
import os
import sys
import shutil
import stat

import re

#CaptureFrom = os.path.normpath("C:/Users/jerry.xie/AppData/Local/Google/Chrome/User Data/Default/Pepper Data/Shockwave Flash")
CaptureFrom = os.path.normpath("C:/Users/Yan/AppData/Local/Google/Chrome/User Data/Default/Pepper Data/Shockwave Flash")
CaptureTo = os.path.normpath("c:/media/temp")
#CaptureTo = "D:\\movie\\friends\\temp"
# "c:/media/temp"
CaptureLog = ""

CaptureEnable=True

def initCapLog():
    global CaptureLog
    CaptureLog = "Check Chrome Cache.\nFrom: " + CaptureFrom + "\nTo:   " + CaptureTo + \
                 "\n-------------------------\n  From  \t->  To\n"


def capChrmFlv(targetName=""):
    global CaptureLog

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

    '''
    print("Check Chrome Cache.")
    print("From: ", CaptureFrom)
    print("To:   ", CaptureTo)
    print("-"*50)
    print("  From  \t->  To")
    '''

    initCapLog()
    print(CaptureLog)

    i = 0
    while True:
        if not CaptureEnable:
            CaptureLog = ""
            break

        for f in os.listdir(CaptureFrom):
            if f.endswith(".tmp"):
                #fromf = CaptureFrom + "/" + f
                fromf = os.path.join(CaptureFrom, f)
                #tof = CaptureTo + "/" + f
                tof = os.path.join(CaptureTo, f)
                if os.path.isfile(tof):                                       # same filename exist in capture-to-dir
                    if os.stat(tof).st_size == os.stat(fromf).st_size:        # same size, bypass
                        continue
                try:
                    #shutil.copyfile(fromf, tof)
                    os.chmod(CaptureFrom, stat.S_IROTH)
                    os.chmod(fromf, stat.S_IROTH)
                    shutil.copy(fromf, tof)
                    '''
                    ff=open(fromf,"rb")
                    ft=open(tof, "wb+")
                    ft.write(ff.read())
                    '''
                    print(f, "\t->  ", f)          #print(fromf," -> ", tof)
                    CaptureLog += f + "\t->  " + f
                except Exception as e:
                    print(e)
                    CaptureLog += str(e)
        time.sleep(1)
        i += 1
        #if (i >= 300):
        #    break

def getCaptureLog():
    global CaptureLog
    return CaptureLog

def captureEnable(enb=True):
    global CaptureEnable
    if enb == True:
        CaptureEnable = True
    else:
        CaptureEnable = False

if __name__ == "__main__":
    capChrmFlv()