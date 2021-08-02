import os
import stat
import shutil

CaptureFrom = os.path.normpath("C:/Users/Yan/AppData/Local/Google/Chrome/User Data/Default/Pepper Data/Shockwave Flash")
ff = os.path.normpath("C:/Users/Yan/AppData/Local/Google/Chrome/User Data/Default/Pepper Data/Shockwave Flash/1C24.tmp")
ft = os.path.normpath("c:/media/temp/f_008b00")

ff1=os.path.normpath("C:/Users/Yan/AppData/Local/Google/Chrome/User Data/Default/Cache/f_008b00")


#os.chmod(CaptureFrom, stat.)
#st = os.stat(CaptureFrom)
#os.chmod(CaptureFrom, st.st_mode | stat.S_IROTH)
#os.chmod(ff, stat.S_IROTH)
#st = os.stat(ff)
#os.chmod(ff, st.st_mode | stat.S_IROTH | stat.S_IREAD | stat.S_)


#f=open(ff1,"rb")
#f.close()


shutil.copy(ff1,ft)

