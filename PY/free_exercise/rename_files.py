"""
A simple function for batch renaming files.
Support regex in src/dst file names.



"""

import os
import re
import tempfile
import shutil
from typing import List, Tuple


SYMBOLS = ['*', '?']


def check_re(pattern):
    try:
        re.compile(pattern)
        return True
    except Exception:
        return False

def rename(folder: str, src: str, dst: str, overwrite:bool=False, regex: bool=True) -> List[Tuple[str]]:
    if not src or not dst:
        return []
    result = []
    if not folder:
        folder = os.path.curdir
    else:
        folder = os.path.realpath(folder)

    if not os.path.isdir(str(folder)):
        raise ValueError(f'Invalid folder {folder}')
    ns = os.path.realpath(os.path.join(folder,src))
    nd = os.path.realpath(os.path.join(folder,dst))
    if not regex:
        if not os.path.isfile(ns) or not os.path.exists(ns):
            raise ValueError(f'Invalid src {ns}')
        if not os.path.isfile(ns):
            raise()
        if os.path.exists(nd) and not overwrite:
            raise Exception(f'Target file {dst} exists, skip.')
        nd = os.path.realpath(dst)
        os.rename(ns, nd)
        return [(ns, nd)]
    comp = re.compile(pattern=src)
    for f in os.listdir(folder):
        file = os.path.join(folder, f)
        if not os.path.isfile(file):
            continue
        match = comp.search(file)
        if not match:
            continue
        try:
            f2 = match.expand(dst)
            new_name = os.path.join(folder, f2)
            if os.path.isdir(new_name):
                print(f'Invalid new name, {new_name} exists as a dir, skip...')
                continue
            if os.path.exists(new_name):
                if overwrite:
                    os.remove(new_name)
                else:
                    raise Exception(f'Cannot rename {f} to {f2}, file exists.')
            os.rename(file, new_name)
            result.append((file, new_name))
        except Exception as e:
            raise Exception('Cannot rename {f} to {new_name}') from e
    return result

def filename_replace(folder:str, charmap:dict) -> List:
    """Replace the characters for the filenames in the given path per the charmap."""
    result = []
    def char_replace(s:str, charmap:dict) -> str:
        dst = s
        for d1, d2 in charmap.items():
            if d1 in dst:
                dst = s.replace(d1, d2)
        return dst

    folder = os.path.realpath(folder)
    for f in os.listdir(folder):
        f = os.path.join(folder, f)
        if os.path.isfile(f):
            src = dst = f
            dst = char_replace(src, charmap)
            os.rename(src, dst)
            result.append((src, dst))
            print(f'renaming: {src} -> {dst}')
    return result
            
def test():
    files = []
    folder = tempfile.TemporaryDirectory()
    print(f'temp folder: {folder.name}')
    for c in ['a', 'b']:
        for i in range(3):
            fn = f'testfile_{c}_{i}.txt'
            file = os.path.join(folder.name, fn)
            with open(file, '+tw') as f:
                f.write(f'{c}{c} {i}{i}')
                print(f'create test file {fn}')
                files.append(fn)

    src, dst  =  r'.*_(\w*)_(\d*).*\.(.*)$', r'tf_\1\1_\2.\3'
    result = rename(folder.name, src, dst)
    print(f'renaming: {src} -> {dst}')
    for s, d in result:
        print(f'  {s} --> {d}')
    print(f'removing temp folder {folder}')
    shutil.rmtree(folder.name)

def test1():
    files = []
    folder = tempfile.TemporaryDirectory()
    print(f'temp folder: {folder.name}')
    for c in ['a', 'b']:
        for i in range(3):
            fn = f'testfile_{c} _{i}.txt'
            file = os.path.join(folder.name, fn)
            with open(file, '+tw') as f:
                f.write(f'{c}{c} {i}{i}')
                print(f'create test file {fn}')
                files.append(fn)

    src, dst  =  r'(.*) (.*)$', r'\1\2'      # removing space
    result = rename(folder.name, src, dst)
    print(f'renaming: {src} -> {dst}')
    for s, d in result:
        print(f'  {s} --> {d}')
    print(f'removing temp folder {folder}')
    shutil.rmtree(folder.name)

def test3():
    files = []
    result = []
    folder = tempfile.TemporaryDirectory()
    charmap = {'一':'1', '二':'2', '三':'3', '四':'4', '五':'5', '六':'6', }

    print(f'temp folder: {folder.name}')
    for c in ['a', 'b']:
        for d, i in charmap.items():
            fn = f'testfile_{c}_{d}.txt'
            file = os.path.join(folder.name, fn)
            with open(file, '+tw') as f:
                f.write(f'{c}{c} {i}{i}')
                print(f'create test file {fn}')
                files.append(fn)

    result = filename_replace(folder.name, charmap)
    for s, d in result:
        print(f'  {s} --> {d}')
    print(f'removing temp folder {folder}')
    for s, d in result:
        print(f'  {s} --> {d}')
    print(f'removing temp folder {folder}')
    shutil.rmtree(folder.name)
    
def test4():
    folder = 'C:\movie\temp'
    charmap = {'一':'1', '二':'2', '三':'3', '四':'4', '五':'5', '六':'6', }
    result = filename_replace(folder, charmap)
    for s, d in result:
        print(f'  {s} --> {d}')


if __name__ == '__main__':
    test3()
