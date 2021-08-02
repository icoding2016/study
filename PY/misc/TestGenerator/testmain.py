#!/usr/bin/env python3

from common import *
from testdata_nrb200ui import *
from testgen import *

'''
from __future__ import print_function

import sys
import os
import platform


from shutil import copyfile

# For pythen 2 and 3 compatibility
try:
        from urllib.request import urlopen, URLopener
        from urllib.parse import urlparse
except ImportError:
        from urllib import urlopen, URLopener
        from urlparse import urlparse

try:
        from http.client import HTTPConnection, HTTPResponse, HTTPException, IncompleteRead
except ImportError:
        from httplib import HTTPConnection, HTTPResponse, HTTPException, IncompleteRead

try:
        from subprocess import getstatusoutput, getoutput, Popen, PIPE, STDOUT
except:
        from commands import getstatusoutput, getoutput 
        from os import popen

# WebSocket lib
try:
        from ws4py.websocket import WebSocket
        from ws4py.client.threadedclient import WebSocketClient
except ImportError:
        sys.path.append(ws4py_path)
        from ws4py.websocket import WebSocket
        from ws4py.client.threadedclient import WebSocketClient

# for platform compatiblity
if platform.system().lower() == 'windows':
        #ws4py_path = "C:\\DEV\\Python\\pkgs\\WebSocket-for-Python-master\\ws4py"
        PATHSPLITER="\\"
else:
        #ws4py_path="\/usr\/local\/lib\/python2.7\/dist-packages\/ws4py"
        PATHSPLITER="/"

####### Debugging functions #######
def _FuncName():
    import traceback
    return traceback.extract_stack(None, 2)[0][2]

dbgFlag = True
def TRACE(str):
    if dbgFlag:
        print("[%s] %s" % (_FuncName(), str))

'''

#######################################################################        
def debugging():
    '''
    #feature1 = FeatureTask("WrongFeature")
    feature2 = FeatureTask("CellScan")
    function = FunctionTask("CellIdDisplay", "CellStat")
    tsklist.append(feature2)
    tsklist.append(function)

    # test ImportTask
    print("="*30)
    gen.ImportTasks(tsklist)
    print(gen._TaskList)
    '''


    '''debugging()
    print(Generator.__class__.__name__)
    print(FeatureSet.__class__.__name__)
    print(FeatureSet["CellScan"].__class__.__name__)
    print("Generator: %s" % (Generator.__class__.__name__))
    print("FeatureSet %s" % (FeatureSet.__class__.__name__))
    print("FeatureSet[xx] %s" % (FeatureSet["CellScan"].__class__.__name__))
    print("object gen: %s" % (gen.__class__.__name__))
    print("object feature2: %s" % (feature2.__class__.__name__))
    print("object function: %s" % (function.__class__.__name__))
    '''

#########################################################################

def nrb200UIDataGeneration():
    TRACE("[nrb200UIDataGeneration]: ")
    
    # Initiate test tasklist
    tsklist = []

    print("="*30)
    tsklist = [ "Battery", "CellStat", "CellStat.CellIdDisplay" ]
    gen.ImportTasksFromNamelist(tsklist)

    print("-"*30)
    PrintGeneratorTaskList(gen)

    print("="*30)
    gen.Run()

    # test

        
#######################################################################        

if __name__ == '__main__':

    
    #testgen.FeatureSet = FeatureSet_nrb200
    #testgen.FeatureName = FeatureName_nrb200
    RegistFeatureSet(FeatureSet_nrb200)
    RegistHandlerDict(TestHandler_nrb200)

    # ...
    gen = Generator()
    gen.WorkMode = "WrongMode"
    gen.WorkMode = "LOOP"     #"RUNONCE"
    print("gen.WorkMode %s" % (gen.WorkMode))

    nrb200UIDataGeneration()


