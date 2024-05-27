import pygetwindow as gw
import pyautogui
import psutil
import subprocess 
import time
import random
import argparse
from pywinauto.application import Application, ProcessNotFoundError
from os import path
from typing import Iterable
from pprint import pprint


def rand_char():
    while True:
        yield  random.choice([chr(i) for i in range(ord('A'), ord('z')+1)])


def gen_char(src:Iterable=None, interval:int=-1, repeat:bool=True):
    """ generate char per src or randomly (if no src)

        if interval < 0, then use random interval 
          interval: -1, (0.05~0.5)
                    -2, (0.5~5)
                    other -n, (2-20)
        if src provided then generate char from src
        if repeat, then use src repeatly
    """
    def _gen_c(src, low, high, latency_factor):
        for c in src:
            delay = random.randint(low, high) * latency_factor
            time.sleep(delay)
            yield c
    if not src:
        src = rand_char()
    delay = interval
    if interval >= 0:
        low, high, latency_factor = interval, interval, 1
    elif interval == -1:
        low, high, latency_factor = 1, 10, 0.05
    elif interval == -2:
        low, high, latency_factor = 1, 10, 0.5
    else:
        low, high, latency_factor = 1, 10, 2
    if repeat:
        while True:
            for c in _gen_c(src, low, high, latency_factor):
                yield c
    else:
        for c in _gen_c(src, low, high, latency_factor):
            yield c


def get_window(title:str, exact_match=True):
    windows = gw.getAllWindows()
    if not title:
        return windows
    if exact_match:
        for w in windows:
            if w.title.lower() == title.lower():
                return [w, ]
    return gw.getWindowsWithTitle(title)
    
def txtbot(timeout:int=0, src:Iterable=None):
    """simulate text input to notepad

    Args:
        timeout (int, optional): the life time of the bot. Defaults to 0 (no kill).
        src (Iterable, optional): the src of input data. Defaults to None (random).

    Raises:
        Exception: _description_
    """
    app_name:str='notepad.exe'
    win_title:str='Untitled - Notepad'
    new_title = '# bnote'
    proc = None

    for p in psutil.process_iter(['name']):
        if p.info['name'] == app_name:
            proc = p
            break
    if not proc:
        app = subprocess.Popen([app_name])
        time.sleep(5)
    wins = get_window('Notepad', exact_match=False)
    if wins:
        win = wins[0]
        win.activate()
        pyautogui.hotkey('ctrl', 'n')
        time.sleep(1)
    else:
        raise Exception(f"Cannot find newlly created window {win_title} for app {app_name}")

    start_time = time.time()
    wins = get_window(win_title, exact_match=True)
    wins[0].activate()
    pyautogui.write(f'{new_title}\n\n', interval=0.05)
    for c in gen_char(src=src, interval=-1):
        if time.time() - start_time > timeout:
            break
        wins = get_window(new_title, exact_match=True)
        wins[0].activate()
        pyautogui.write(c)


def run():
    # windows = get_window('');    pprint([w.title for w in windows])
    src = None
    with open(path.abspath(__file__), 'r') as f:
        src = f.read()
    txtbot(timeout=20000, src=src)


def app():
    parser = argparse.ArgumentParser()

    parser.add_argument('-l', '--lifetime', type=int, default=0, required=False)
    parser.add_argument('-f', '--file_name', type=str, default=None, required=False)
    args = parser.parse_args()

    timeout = args.lifetime
    src_file = args.file_name
    src = None
    if src_file:
        fn = path.realpath(src_file)
        with open(fn, 'r') as f:
            src = f.read()
    txtbot(timeout, src)



if __name__ == '__main__':
    # run()
    app()



