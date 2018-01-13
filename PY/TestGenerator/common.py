#!/usr/bin/env python3
#
# Common define & functions
#

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

'''
# WebSocket lib
try:
        from ws4py.websocket import WebSocket
        from ws4py.client.threadedclient import WebSocketClient
except ImportError:
        sys.path.append(ws4py_path)
        from ws4py.websocket import WebSocket
        from ws4py.client.threadedclient import WebSocketClient
'''

# for platform compatiblity
if platform.system().lower() == 'windows':
        #ws4py_path = "C:\\DEV\\Python\\pkgs\\WebSocket-for-Python-master\\ws4py"
        PATHSPLITER="\\"
else:
        #ws4py_path="\/usr\/local\/lib\/python2.7\/dist-packages\/ws4py"
        PATHSPLITER="/"

####### Debugging functions #######

import traceback

dbgFlag = True
stackFlag = False

def TRACE(str):
    if dbgFlag:
        if stackFlag:
            print("[%s,%s] %s" % (traceback.extract_stack(None, 2)[0][2],traceback.extract_stack(None, 2)[0][1], str))
        else:
            print(str)




