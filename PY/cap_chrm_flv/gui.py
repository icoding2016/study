#!/usr/bin/python3

from tkinter import *

import cap_chrm_flv
#from cap_chrm_flv import capChrmFlv


class App(Frame):
    STATE = {"RUNNING", "STOP"}
    state = "STOP"
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
        self.state = "STOP"

    def create_widgets(self):
        self.button_run = Button(self, text="Stopped")
        self.button_run.grid()
        self.button_run["command"] = self.button_run_click

        self.labelfrm = LabelFrame(self)
        self.labelfrm.grid()

        self.label_log = Label(self.labelfrm, text="log text." )
        self.label_log.grid()
        #self.labelfrm.pack(fill="both", expand="yes")

    def button_run_click(self):
        if self.state == "STOP":
            self.state = "RUNNING"
            # run func
            cap_chrm_flv.captureEnable(True)
            cap_chrm_flv.capChrmFlv()
            self.button_run["text"] = "Running"
        else:  # Running
            self.state = "STOP"
            # stop func
            cap_chrm_flv.captureEnable(False)
            self.button_run["text"] = "Stopped"

    def pannel_log_update(self):
        #self.
        pass


############################################################
root = Tk()
root.title("Chrome Cache Collector")
root.geometry("300x200+50+50")

app = App(root)
app.grid()

root.mainloop()

