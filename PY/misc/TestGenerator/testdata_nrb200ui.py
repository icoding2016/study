#!/usr/bin/env python3

from common import *

#########################################################################
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


# for platform compatiblity
if platform.system().lower() == 'windows':
        #ws4py_path = "C:\\DEV\\Python\\pkgs\\WebSocket-for-Python-master\\ws4py"
        PATHSPLITER="\\"
else:
        #ws4py_path="\/usr\/local\/lib\/python2.7\/dist-packages\/ws4py"
        PATHSPLITER="/"

import testgen
'''
#########################################################################
# Test Data definition
# 
'''
check points (UI data display):
[DataEntry]
- Data input validation on CellID / RSRP
- Apply & ?

[Battery]
- Battery status
  Capacity: (0-100%); Status: fully charged/charging/error;  Bar:

[CellScan]
- Cell ID.   with both PCI/ECGI, and different MCC/MNC
- RSRP/RSRQ/SINR,
- RSRP threshold change per Data entry
  bar indicator/ color & txt
- show all wll cells?
- display order
- servicing cell flag @ cell_switching
- band 2 & 30

[CellStat]
- Cell ID
- RSRP/RSRQ min/max/ave
- Sample#
- Rerun

[TputTest]  
- Tput test pass(U&D) / fail(U&D) / part fail (U|D).
  Color/bold on result text
- Test result kept untill next
- Tput test timeout.
- Datalink broke during Tput test.
- Tput test @ cell switching  
- Entry data changed during Tput test
- Tput test on different file types ?
- Tput test multiple times ?

[Report]
- Pass/Fail in scan & tput
- Report upload to AT&T server. with specific dir and access.
- Naming rule.   SN/DateTime/version#
'''

#FeatureName_nrb200 = { "DataEntry", "Battery", "CellScan", "CellStat", "TputTest", "Report" }
FeatureSet_nrb200 = {  
    # Feature:{ Function1, Function2, ...}
    "DataEntry":{  "CellIdInput",
                   "RsrpInput",
                },
    "Battery":  {  "BatteryStatus",
                   #"",
                },
    "CellScan": {  "CellIdDisplay",
                   "CellSignalDisplay",
                   "ResultDisplayPerRsrp",
                   "CellDisplayOrder",
                   "ShowAllCells",
                   "ServingCellChange",
                   "MultiBands",
                },
    "CellStat": {  "CellIdDisplay",
                   "CellSignalDisplay",
                   "Rerun",
                },
    "TputTest": {  "TputTestResult",
                   "ResultKeptUntilNextTest",
                   "TputTestTimeout",
                   "DatalinkBrokeDuringTputTest",
                   "CellSwitchDuringTputTest",
                   "EntyDataChangeDuringTputTest",
                   "TputTestOnMultiFileTypes",
                   "TputTestMultiTimes",
                },
    "Report":   {  "ScanResult",
                   "ReportUploadToSvr",
                   #"NamingRule",
                },

    }

'''
FeatureTestHandler_nrb200 = {
    # "Feature1":{ "Function1":"Feature1_Functin1_Handler", 
    #              "Function2":"Feature1_Function2_Handler", ...}
    # e.g.
    #"DataEntry":{  "CellIdInput":"DataEntry_CellIdInput_Handler",
    #               "RsrpInput":"DataEntry_RsrpInput_Handler",
    #            },
    #"Battery":  {  "BatteryStatus":"Battery_BatteryStatus_Handler"
    #               #"",
    #            },
    }
'''


TestHandlerName_nrb200 = {
 'Battery_BatteryStatus_Handler',                
 'TputTest_TputTestTimeout_Handler',
 'CellScan_CellDisplayOrder_Handler',
 'TputTest_TputTestMultiTimes_Handler',
 'TputTest_CellSwitchDuringTputTest_Handler',
 'TputTest_ResultKeptUntilNextTest_Handler',
 'CellScan_ShowAllCells_Handler',
 'DataEntry_RsrpInput_Handler',
 'CellStat_CellSignalDisplay_Handler',
 'CellScan_ServingCellChange_Handler',
 'CellScan_MultiBands_Handler',
 'TputTest_TputTestOnMultiFileTypes_Handler',
 'CellScan_CellSignalDisplay_Handler',
 'CellStat_CellIdDisplay_Handler',
 'Report_ScanResult_Handler',
 'CellStat_Rerun_Handler',
 'DataEntry_CellIdInput_Handler',
 'TputTest_TputTestResult_Handler',
 'CellScan_ResultDisplayPerRsrp_Handler',
 'CellScan_CellIdDisplay_Handler',
 'TputTest_DatalinkBrokeDuringTputTest_Handler',
 'TputTest_EntyDataChangeDuringTputTest_Handler'
 'Report_ReportUploadToSvr_Handler',
}

#########################################################################
# Test Handlers

def DataEntry_CellIdInput_Handler():
    TRACE("Not implemented")
    pass

def DataEntry_RsrpInput_Handler():
    TRACE("Not implemented")
    pass

def Battery_BatteryStatus_Handler():
    TRACE("Not implemented")

    pass

def CellScan_ResultDisplayPerRsrp_Handler():
    TRACE("Not implemented")
    pass

def CellScan_CellIdDisplay_Handler():
    TRACE("Not implemented")
    pass

def CellScan_CellDisplayOrder_Handler():
    TRACE("Not implemented")
    pass

def CellScan_ShowAllCells_Handler():
    TRACE("Not implemented")
    pass

def CellScan_CellSignalDisplay_Handler():
    TRACE("Not implemented")
    pass

def CellScan_ServingCellChange_Handler():
    TRACE("Not implemented")
    pass

def CellScan_MultiBands_Handler():
    TRACE("Not implemented")
    pass

def CellStat_CellIdDisplay_Handler():
    TRACE("Not implemented")
    pass

def CellStat_Rerun_Handler():
    TRACE("Not implemented")
    pass

def CellStat_CellSignalDisplay_Handler():
    TRACE("Not implemented")
    pass

def TputTest_TputTestTimeout_Handler():
    TRACE("Not implemented")
    pass

def TputTest_TputTestMultiTimes_Handler():
    TRACE("Not implemented")
    pass

def TputTest_CellSwitchDuringTputTest_Handler():
    TRACE("Not implemented")
    pass

def TputTest_ResultKeptUntilNextTest_Handler():
    TRACE("Not implemented")
    pass

def TputTest_TputTestOnMultiFileTypes_Handler():
    TRACE("Not implemented")
    pass

def TputTest_DatalinkBrokeDuringTputTest_Handler():
    TRACE("Not implemented")
    pass

def TputTest_EntyDataChangeDuringTputTest_Handler():
    TRACE("Not implemented")
    pass

def TputTest_TputTestResult_Handler():
    TRACE("Not implemented")
    pass

def Report_ScanResult_Handler():
    TRACE("Not implemented")
    pass

def Report_ReportUploadToSvr_Handler():
    TRACE("Not implemented")
    pass

global TestHandler_nrb200
TestHandler_nrb200 = {
 "Battery_BatteryStatus_Handler":Battery_BatteryStatus_Handler,                
 "TputTest_TputTestTimeout_Handler":TputTest_TputTestTimeout_Handler,
 "CellScan_CellDisplayOrder_Handler":CellScan_CellDisplayOrder_Handler,
 "TputTest_TputTestMultiTimes_Handler":TputTest_TputTestMultiTimes_Handler,
 "TputTest_CellSwitchDuringTputTest_Handler":TputTest_CellSwitchDuringTputTest_Handler,
 "TputTest_ResultKeptUntilNextTest_Handler":TputTest_ResultKeptUntilNextTest_Handler,
 "CellScan_ShowAllCells_Handler":CellScan_ShowAllCells_Handler,
 "DataEntry_RsrpInput_Handler":DataEntry_RsrpInput_Handler,
 "CellStat_CellSignalDisplay_Handler":CellStat_CellSignalDisplay_Handler,
 "CellScan_ServingCellChange_Handler":CellScan_ServingCellChange_Handler,
 "CellScan_MultiBands_Handler":CellScan_MultiBands_Handler,
 "TputTest_TputTestOnMultiFileTypes_Handler":TputTest_TputTestOnMultiFileTypes_Handler,
 "CellScan_CellSignalDisplay_Handler":CellScan_CellSignalDisplay_Handler,
 "CellStat_CellIdDisplay_Handler":CellStat_CellIdDisplay_Handler,
 "Report_ScanResult_Handler":Report_ScanResult_Handler,
 "CellStat_Rerun_Handler":CellStat_Rerun_Handler,
 "DataEntry_CellIdInput_Handler":DataEntry_CellIdInput_Handler,
 "TputTest_TputTestResult_Handler":TputTest_TputTestResult_Handler,
 "CellScan_ResultDisplayPerRsrp_Handler":CellScan_ResultDisplayPerRsrp_Handler,
 "CellScan_CellIdDisplay_Handler":CellScan_CellIdDisplay_Handler,
 "TputTest_DatalinkBrokeDuringTputTest_Handler":TputTest_DatalinkBrokeDuringTputTest_Handler,
 "TputTest_EntyDataChangeDuringTputTest_Handler":TputTest_EntyDataChangeDuringTputTest_Handler,
 "Report_ReportUploadToSvr_Handler":Report_ReportUploadToSvr_Handler,
}

#########################################################################


# rdb definition

rdbName = { "rdb_cell_qty":'wwan.0.cell_measurement.qty',                           
            "rdb_cell_status":'wwan.0.cell_measurement.status',                     
            "rdb_cell_measurement_prefix":'wwan.0.cell_measurement.',               
            "rdb_batt_charge_percentage":'service.nrb200.batt.charge_percentage',   
            "rdb_batt_status":'service.nrb200.batt.status',                         
            "rdb_rrc_qty":'wwan.0.rrc_info.cell.qty',                               
            "rdb_rrc_prefix":'wwan.0.rrc_info.cell.'                                
         }  

# Cells to simulate in the 'Cell Scan Scenario'
CellInfo = ( # channel,   PCI,     CellID
             { "CH":902, "PCI":2, "CID":27447302 },
             { "CH":903, "PCI":3, "CID":27447303 },
             { "CH":904, "PCI":4, "CID":27447304 },
             { "CH":905, "PCI":5, "CID":27447305 },
             { "CH":906, "PCI":6, "CID":27447306 },
             { "CH":907, "PCI":7, "CID":27447307 },
             { "CH":908, "PCI":8, "CID":27447308 },
             { "CH":909, "PCI":9, "CID":27447309 },
             { "CH":910, "PCI":10, "CID":27447310 },
             { "CH":911, "PCI":11, "CID":27447311 },
             { "CH":912, "PCI":12, "CID":27447312 },
          )





#########################################################################

def RemoteAdbCmd(cmdStr):
    cmd = "adb shell " + cmdStr

    status, output = getstatusoutput(cmd)
    print(output, end="")

    return status







    
    
