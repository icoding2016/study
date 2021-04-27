import threading
import time


class MyThread(threading.Thread):
   
    def __init__(self, group=None, target=None, name=None, args=(), kwargs={}):
        super().__init__(group, target, name, args, kwargs)
        self.heart_beat = 3
        self.event = args[1]
        self.terminate = False


    def run(self):
        super().run()
        while(not self.terminate):
            print("Heart beat.")
            time.sleep(self.heart_beat)
            self.CheckEvent()

    def CheckEvent(self):
        if self.event.is_set():
            self.terminate = True
            print("MyThread to be terminated.")


def Test():
    e = threading.Event()
    t = MyThread(e)

    t.start()
    time.sleep(10)

    e.set()




if __name__ == "__main__":
    Test()

