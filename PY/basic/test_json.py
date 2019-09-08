
def TestJson():
    STRUCT = """{
  "name": "urpf-testing",
  "description": "DPC Testing",
  "created by": "hines",
  "topology": {
    "device_list": [
      {"name":"mx960-6","type":"juniper"},
      {"name":"ixia-term2","type":"ixia","port":"8069"}
    ]
  },
  "test_cases": {
    "1": {"name": "Setup", "args":{}},
    "2": {"name": "AverageMatchEdge", "args":{}},
    "3": {"name": "AverageMatchEdgeuRPF", "args":{}},
    "4": {"name": "TopMatchMinuRPF", "args":{}},
    "5": {"name": "TopMatchEdgeuRPF", "args":{}},
    "6": {"name": "WorstMatchEdgeuRPF", "args":{}},
    "7": {"name": "NoFilter", "args":{}},
    "8": {"name": "TopMatchMin", "args":{}},
    "9": {"name": "EnableuRPF", "args":{}},
    "10": {"name": "WorstMatchEdge", "args":{}},
    "11": {"name": "TopMatchEdge", "args":{}},
    "12": {"name": "Clean", "args":{}}
    },
  "dut_int": {
    "src_list": ["xe-11/0/0"],
    "dest_list": ["xe-11/1/0"]
  },
  "tester_int": {
    "src_list": ["ixia1:3/3"],
    "dest_list": ["ixia1:3/4"]
  }
}
"""

    STRUCT1 = """# Reserved test variables:
"test_title":           "JunOS basic regression test suite",   # Default is script name.
"test_data_dir":        "/home/jou/src/google3/ops/netops/lab/testsuites/testdata",
"test_topology_file":   "junos_regression.topo",
"test_domain":          "net",
"test_log_level":       "debug",          # Default is "DEBUG".
"test_log_stdout":      True,             # Default is True.
"test_log_dir":         "/var/tmp/LOG_smoke_test", # Default is "/var/tmp"
"test_config_cleanup":   True,            # Default is True.
"test_config_commit":    True,            # Default is True.
"test_config_wait":      180,             # Default is 120 second.
"test_cleanup_items":    ['firewall', 'protocols', 'cos', 'isis',
                          'bgp', 'mpls', 'policy' ],
"test_config_items":     ['interface', 'template', 'isis', 'ospf', 'bgp',
                          'mpls'],
"test_config_save":      False,           # Default is True.
"test_config_restore":   False,           # Default is True.
"test_cflowd_addr":      "172.18.88.207", # IP address for junou.mtv.corp.google.com.
"test_chk_link":         True,            # Default is True.
"test_connect_tester":   True,            # Default is True.
"test_mail_addr":        "jou",           # Email id for sending test report.
"test_max_testcases":    100,             # Maximal test case # to run.
"test_chk_status":       True,

# User defined test variables:
"my_ixia_config":        "junos_regression.ixncfg",  # Ixia configuration.
"my_lsp_count":          4,               # Number of LSPs (default is 4)
"my_tester_pps":         668747.45,       # Ixia pps: 20% of 10GE speed
"my_tester_ebgp_duts":     [3, 4],

# Test cases in ChkTestStatus():
"testcase 001": {
  "description": "Check protocol neighbors for all BB/DR routers",
  "callback": "ChkProtNeighbors",
  "chkstatus":  0  # Default is 1.
},
"testcase 002": {
  "description": "Test router reachabilities (ping loopback) between any BB/DR routers",
  "callback": "PingLoopbackIPs",
  "chkstatus": 0
}
"""
    import json
    j1 = json.loads(STRUCT)
    print(j1)
    for n,v in j1.items():
        print("{} = {},   {},{}".format(n,v, type(n), type(v)))


if __name__ == "__main__":
    TestJson()
