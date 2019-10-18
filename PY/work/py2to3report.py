'''
Calculate the PY3 conversion percentage under a given folder (recursively), 

Ideas:
1. Target based:  (converted_targets / all_targets)
   - count all the python 'targets' from BUILD files in the folder (recursively)
   - count converted target (multi-paterns for searching)
     method: match the patern in the test/library/binary target sections:
             - py2and3.*_test vs py_test, for py2and3_test or py2and3_strict_test)
             - srcs_version = "PY2AND3" vs srcs_version = "PY2", for for library/binary

2. File based:    (converted_files / all_files)
   - count all .py files under the folder.
   - count converted .py
     method: The first line of the converted .py has a comment of "# Lint as: python2, python3", 
             However not all .py need conversion and thus not having the lint comment. 
             It cannot give a correct percentage unless we have better method to identify converted py files.



Usage:
  py2to3report <code-path-for-statistics>

'''

import os
import sys
import glob
import re


DEF_WORKSPACE = r"/google/src/cloud/yanxie/smartlab_2to3_b/google3/"
DEF_TARGET_FOLDER = r"ops/netops/lab/b2"
DEF_ROOT_FOLDER = os.path.join(DEF_WORKSPACE, DEF_TARGET_FOLDER)


class Py3Stat(object):
    #pattern_pytarget = r'_library\(|_test\(|_binary\('     # the pattern for all types of Python targets in BUILD, simply for counting
    pattern_pytarget_name = r'(py[\w_]*_binary|py[\w_]*_library|py[\w_]*_test)\(.*\s*name\s*=\s*\"([\w\/]*)\"'     # the pattern for python target names (incl */*) in BUILD
    pattern_py3target_name = r''     # the pattern for python target names (incl */*) in BUILD
    pattern_pytarget_section = r'(py[\w_]*_binary|py[\w_]*_library|py[\w_]*_test)\(.*\s*name\s*=\s*\"([\w\/]*)\"[\s\S]*?\)'
    pattern_pylib_section = r'(py[\w_]*_library)\(.*\s*name\s*=\s*\"([\w\/]*)\"[\s\S]*?\)'
    pattern_pybin_section = r'(py[\w_]*_binary)\(.*\s*name\s*=\s*\"([\w\/]*)\"[\s\S]*?\)'
    pattern_pytest_section = r'(py[\w_]*_test)\(.*\s*name\s*=\s*\"([\w\/]*)\"[\s\S]*?\)'
    pattern_py3test_section = r'(py2and3[\w_]*_test)\(.*\s*name\s*=\s*\"([\w\/]*)\"[\s\S]*?\)'


    def __init__(self, root_folder=DEF_ROOT_FOLDER):
        self.root_folder = os.path.abspath(root_folder)

    def ScanByTarget(self):        
        pass

    def ScanByFiles(self):
        print("not implemented")

    def Report(self):        
        rep1 = ScanByTarget()
        print(rep1)

    def CountTargetsPy(self):
        '''Count the PY target number under the specified folder (recursively)'''
        for fn in glob.iglob(self.root_folder + "**/BUILD", recursive=True):
            print(fn)
            with open(fn, 'rt') as f:
                content = f.read()
                
                alltarget = self._FindPyTarget(content)
                self.count_alltarget = len(alltarget)
                print("all targets count={}".format(self.count_alltarget))
                self._PrintList(alltarget)

                p3test = self._FindPy3Test(content)
                self.count_p3test = len(p3test)
                print("py3 test targets count={}".format(self.count_p3test))
                self._PrintList(p3test)

                return self.count_alltarget



    def _FindPyTarget(self, content):
        '''Find all the python targets in the given content (from a BUILD file)
          content:  the BUILD file content
          return:   a list of found targets
        '''
        if content:
            return re.findall(self.pattern_pytarget_name, content)
        return None

    def _FindPy3Target(self, content):
        '''Find all the python3 targets (lib/bin/test) in the given content (from a BUILD file)
          content:  the BUILD file content
          return:   a list of found targets, None if no content provided
        '''
        if content:
            return re.findall(self.pattern_py3target_name, content)
        return None

    def _FindPy3Test(self, content):
        '''Find all the python3 test targets in the given content (from a BUILD file)
          content:  the BUILD file content
          return:   a list of found targets, None if no content provided
        '''
        if content:
            return re.findall(self.pattern_py3test_section, content)
        return None



    def _PrintList(self, lst):
        if not lst or not isinstance(lst, list):
            return
        for item in lst:
            print("  {}".format(item))



if __name__ == "__main__":

    if len(sys.argv) > 1:
        rootdir = sys.argv[1]
        p3stat = Py3Stat(root_folder=rootdir)
    else:
        p3stat = Py3Stat()

    p3stat.CountTargetsPy()
    #p3stat.Report()

