

import time
import os
import sys
import shutil
import stat
import json


'''
dir_chrome_cache=os.path.normpath("C:/Users/Yan/AppData/Local/Google/Chrome/User Data/Default/Cache")
dir_chrome_flv=os.path.normpath("C:/Users/Yan/AppData/Local/Google/Chrome/User Data/Default/Pepper Data/Shockwave Flash")
dir_firefox=os.path.normpath("C:/Users/Yan/AppData/Local/Mozilla/Firefox/Profiles/7k6p8x5k.default/cache2/entries")

dir_save_root = os.path.normpath("c:/media/cap")
dir_save_chrome = os.path.join(dir_save_root, "chrome")
dir_save_chromeflv = os.path.normpath(dir_save_root, "chromeflv")
dir_save_ffox = os.path.normpath(dir_save_root, "ffox")


dirs_cfg = [ # (from, to)
    (dir_chrome_cache, dir_save_chrome, ),
    (dir_chrome_flv, dir_save_chromeflv),
    (dir_firefox, dir_save_ffox),
    ]

dirs_to_capture = []
'''

CaptureLog = ""

CaptureEnable=True

def initCapLog():
    global CaptureLog
    CaptureLog = "\n-------------------------\n  From  \t->  To\n" #"Check Cache.\nFrom: " + CaptureFrom + "\nTo:   " + CaptureTo + \

class Config(object):

    _default_cfg = {
        "time_filter": True,
        "time_delta":0,         # min
        "size_filter": True,
        "size_threshold": 512,  # K
        "monitor_list": ["dir_chrome_cache", "dir_chrome_flv", "dir_firefox"],
        "dir_chrome_cache": os.path.normpath("C:/Users/Yan/AppData/Local/Google/Chrome/User Data/Default/Cache"),
        "dir_chrome_flv": os.path.normpath("C:/Users/Yan/AppData/Local/Google/Chrome/User Data/Default/Pepper Data/Shockwave Flash"),
        "dir_firefox": os.path.normpath("C:/Users/Yan/AppData/Local/Mozilla/Firefox/Profiles/7k6p8x5k.default/cache2/entries"),
        "dir_save_root": os.path.normpath("c:/media/cap"),
        # "dir_save_chrome" = os.path.join(dir_save_root, "chrome")
        # "dir_save_chromeflv" = os.path.normpath(dir_save_root, "chromeflv")
        # "dir_save_ffox" = os.path.normpath(dir_save_root, "ffox")
    }

    def __init__(self):
        self._cfg_file_name = "cap_mv.cfg"
        self._cfg_file_path = os.path.join(os.path.curdir, self._cfg_file_name)
        self._cfg_data = self._default_cfg

        if not os.path.exists(self._cfg_file_path):
            print("Cfg file not found, create default: %s" % self._cfg_file_path)
            with open(self._cfg_file_path, "w+") as f:  # create default config file (json)
                json.dump(self._cfg_data, f)

    def load_cfg_file(self):
        with open(self._cfg_file_path,"r") as f:
            self._cfg_data = json.load(f)

    def save_cfg_file(self):
        with open(self._cfg_file_path,"r") as f:
            json.dump(self._cfg_data, f)

    def get_cfg(self):
        return self._cfg_data

    def restore_default(self):
        self._cfg_data = self._default_cfg

    def print_cfg(self):
        for (k,v) in self._cfg_data.items():
            print("%s:\t%s" % (k, v))


def cap_mv(t=None, s=None):
    global CaptureLog
    
    cfg = Config()
    cfg.load_cfg_file()
    cfg_data = cfg.get_cfg()
    cfg.print_cfg()
    
    # init save_to dir
    dirs_cfg = [  # (from, to)
        (cfg_data["dir_chrome_cache"], os.path.join(cfg_data["dir_save_root"],"chrome")),
        (cfg_data["dir_chrome_flv"], os.path.join(cfg_data["dir_save_root"],"chromeflv")),
        (cfg_data["dir_firefox"], os.path.join(cfg_data["dir_save_root"],"firefox")),
        ]
    dirs_to_capture = [] 
    for (df, dt) in dirs_cfg:
        try:
            if (not os.path.exists(df)) \
                    or (not os.path.isdir(df)):
                print("Capture path not exist or not a directory: ", df)
            else:
                os.makedirs(dt, exist_ok=True)
                dirs_to_capture.append((df, dt))
                print("Monitoring dir: \n [monitor]%s\n[copy_to]" % (df, dt))
        except Exception as e:
            print(e)

    starttime = time.time()
    deltatime = cfg_data["time_delta"]*60  # sec
    monitetime = starttime + deltatime
    print("Program start: %s\n, deltatime: %s (min)\nMoniteStart:%s" %
          (time.strftime("%H:%M:%S",time.localtime(starttime)),
           cfg_data["time_delta"],
           time.strftime("%H:%M:%S",time.localtime(monitetime))))

    initCapLog()
    print(CaptureLog)

    i = 0
    while True:
        if not CaptureEnable:
            CaptureLog = ""
            break

        monitering = False
        for (CaptureFrom, CaptureTo) in dirs_to_capture:
            for moniPathTag in cfg_data["monitor_list"]:
                if CaptureFrom == cfg_data[moniPathTag]:                   # Filter out un-selected target
                    monitering = True
                    break

            if not monitering:
                continue

            os.chdir(CaptureFrom)
            for f in os.listdir(CaptureFrom):
                #if f.endswith(".tmp"):
                if os.path.isdir(f):
                    continue
                fromf = os.path.join(CaptureFrom, f)
                tof = os.path.join(CaptureTo, f)

                try:
                    st = os.stat(fromf)
                    if st.st_mtime < monitetime:                       # Only capture the new files created after capture start
                        continue

                    if st.st_size < cfg_data["size_threshold"]*1024:
                        continue

                    if os.path.isfile(tof):                                       # same filename exist in capture-to-dir
                        if os.stat(tof).st_size == os.stat(fromf).st_size:        # same size, bypass
                            continue
                except Exception as e:
                    print(e)
                    CaptureLog += str(e)
                    
                try:
                    #os.chmod(CaptureFrom, stat.S_IROTH)
                    #os.chmod(fromf, stat.S_IROTH)
                    shutil.copy(fromf, tof)
                    txt = f + "\t" + fromf + " -> " + tof
                    print(txt)          #print(fromf," -> ", tof)
                    CaptureLog += txt
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
    if len(sys.argv)>=2:
        if sys.argv[1].startswith('-'):
            option = sys.argv[1][1:]
            # fetch sys.argv[1] but without the first two characters
            if option == 't' or option =='time':  # -- version
                tm = sys.argv[2]
                print("time=", tm)
                'Version 1.2'
            elif option == 'help':  # --help
                pass

    cap_mv()


