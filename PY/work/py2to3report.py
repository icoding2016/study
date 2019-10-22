'''
Calculate the PY3 conversion percentage under a given folder (recursively), 

Ideas:
1. Target based:  (converted_targets / all_targets)
   - count all the python 'targets' from BUILD files in the folder (recursively)
       py*_library,  (py_library/py_strict_library/pytype_library/pytype_strict_library)
       py*_binary, 
       py*_test (could be py_test/py_strict_test/pytype_test/pytype_strict_test/py2and3_test/py2and3_strict_test)
   - count converted target (multi-paterns for searching)
     method: match the patern in the test/library/binary target sections:
        - for test: 
          PY3: py2and3.*_test or py[type][_strict]_test with 'python_version = "PY3"'
          PY2: py[type][_strict]_test with 'python_version = "PY2" or no python_version
        - for lib/bin
          srcs_version = "PY2AND3" vs srcs_version = "PY2"; the 'srcs_version' tag may not exist (considered as python2 before conversion)
          python_version = "PY2" or "PY3" (optional, for more common cases the tag does not exist)

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
    pattern_pytarget = r'(py\w*_binary|py\w*_library|py\w*_test)\(.*\s*name\s*=\s*\"([\w\/]*)\"'     # the pattern for python target names (incl */*) in BUILD
    pattern_pytarget_test = r'(py\w*_test)\(.*\s*name\s*=\s*\"(.*)\",'                  # group: (target_type, target_name)
    pattern_pytarget_lib  = r'((py\w*_library)\(.*\s*name\s*=\s*\"(.*)\",\s*[\s\S]*?srcs_version\s*=\s*"(\w*)",\s*[\s\S]*?\))'      # group: (the whole section, target_type, name, srcs_version)
    #pattern_pytarget_bin  = r'(py\w*_linary)\(.*\s*name\s*=\s*\"(.*)\",'                # group: (target_type, target_name)
    pattern_pytest_section = r'(py\w*_test\(.*\s*name\s*=\s*\"[\w\/]*\"[\s\S]*?\))'          # group: (the whole section)
    pattern_pylib_section  = r'((py\w*_library)\(.*\s*name\s*=\s*\"(.*)\",\s*[\s\S]*?\))'    # group: (the whole section, target_type, name)
    pattern_pybin_section  = r'((py\w*_binary)\(.*\s*name\s*=\s*\"([\w\/])*\"[\s\S]*?\))'    # group: (the whole section, target_type, name)
    pattern_py2and3test = r'(py2and3\w*_test)\(.*\s*name\s*=\s*\"([\w\/]*)\"[\s\S]*?\)' # group: (target_type, target_name)
    pattern_pytest_py3 = r'(py_test|py[^2]\w*_test)\(.*\s*name\s*=\s*\"(.*)\"[\s\S]*?python_version\s*=\s*\"PY3\",'  # group: (target_type, target_name)
    pattern_srcver = r'srcs_version\s*=\s*\"(\w*)\",'                                   # group (src_version), may not exist.
    pattern_pyver  = r'python_version\s*=\s*\"(\w*)\",'                                 # group (python_version), may not exist.


    def __init__(self, root_folder=DEF_ROOT_FOLDER):
        self.root_folder = os.path.abspath(root_folder)
        self.report = ''

        self.alltarget = []
        self.pytests = []
        self.pylibs = []
        self.pybins = []
        self.count_alltarget = 0    # global counter
        self.count_all3target = 0    # global counter
        self.count_all2target = 0    # global counter
        self.count_py2test = 0
        self.count_py3test = 0
        self.count_pytest = 0
        self.count_py2lib = 0
        self.count_py3lib = 0
        self.count_pylib = 0
        self.count_py2bin = 0
        self.count_py3bin = 0
        self.count_pybin = 0

        self.sub_pyfolders = []
        self.count_pymoudels = 0

    def ScanByTarget(self):
        self.LogReport("==PY3 conversion report by targets==\n")
        for fn in glob.iglob(os.path.join(self.root_folder, "**/BUILD"), recursive=True):
            with open(fn, 'rt') as f:
                content = f.read()

                self.LogReport("-"*60 + "\n")
                self.LogReport("Scan {}:\n".format(fn))

                # scan py tests
                py3tests, py2tests = self._ScanPyTestInContent(content)
                count_py2test = len(py2tests)
                count_py3test = len(py3tests)
                count_pytest  = count_py3test + count_py2test
                self.LogReport(py3tests)
                self.LogReport(py2tests)
                self.LogReport("\n")

                self.pytests   += py3tests + py2tests
                self.alltarget += py3tests + py2tests
                self.count_py2test += count_py2test
                self.count_py3test += count_py3test
                self.count_pytest  += count_pytest

                # scan py lib
                py3libs, py2libs = self._ScanPyLibInContent(content)
                count_py2lib = len(py2libs)
                count_py3lib = len(py3libs)
                count_pylib = count_py3lib + count_py2lib
                self.LogReport(py3libs)
                self.LogReport(py2libs)
                self.LogReport("\n")

                self.pylibs    += py3libs + py2libs
                self.alltarget += py3libs + py2libs
                self.count_py2lib += count_py2lib
                self.count_py3lib += count_py3lib
                self.count_pylib  += count_pylib

                # scan py bin
                py3bins, py2bins = self._ScanPyBinInContent(content)
                count_py2bin = len(py2bins)
                count_py3bin = len(py3bins)
                count_pybin = count_py3bin + count_py2bin
                self.LogReport(py3bins)
                self.LogReport(py2bins)
                self.LogReport("\n")

                self.pybins    += py3bins + py2bins
                self.alltarget += py3bins + py2bins
                self.count_py2bin += count_py2bin
                self.count_py3bin += count_py3bin
                self.count_pybin  += count_pybin

                # local summary (targets in current dir)
                count_localtarget = count_pylib + count_pytest + count_pybin
                count_localtarget_py3 = count_py3lib + count_py3test + count_py3bin
                count_localtarget_py2 = count_py2lib + count_py2test + count_py2bin

                self.count_alltarget += count_localtarget
                self.count_all3target += count_localtarget_py3
                self.count_all2target += count_localtarget_py2

                self.LogReport('  ' + '-'*20 + "\n")
                self.LogReport("    Targets in current dir:{},  PY3:{}  PY2:{}\n".format(count_localtarget, count_localtarget_py3, count_localtarget_py2))
                self.LogReport("    lib  targets-- PY3:{}/{}, PY2:{}/{}\n".format(count_py3lib, count_pylib, count_py2lib, count_pylib))
                self.LogReport("    bin  targets-- PY3:{}/{}, PY2:{}/{}\n".format(count_py3bin, count_pybin, count_py2bin, count_pybin))
                self.LogReport("    test targets-- PY3:{}/{}, PY2:{}/{}\n".format(count_py3test, count_pytest, count_py2test, count_pytest))
                self.LogReport("\n")

                if count_localtarget > 0:
                    self.sub_pyfolders.append(fn)
                    self.count_pymoudels += 1
                
        
        self.LogReport('\n' + '='*80 + "\n")
        self.LogReport("Scanned folder:{}\n".format(self.root_folder))
        self.LogReport("  Python modules (BUILD): {}\n".format(self.count_pymoudels))
        for folder in self.sub_pyfolders:
            self.LogReport("    {}\n".format(folder))
        self.LogReport("\n  PY2->3 statistic\n")
        self.LogReport("    lib  targets--\tPY3:{}/{},\tPY2:{}/{}\n".format(self.count_py3lib, self.count_pylib, self.count_py2lib, self.count_pylib))
        self.LogReport("    bin  targets--\tPY3:{}/{},\tPY2:{}/{}\n".format(self.count_py3bin, self.count_pybin, self.count_py2bin, self.count_pybin))
        self.LogReport("    test targets--\tPY3:{}/{},\tPY2:{}/{}\n".format(self.count_py3test, self.count_pytest, self.count_py2test, self.count_pytest))
        self.LogReport("  Total targets: {},\tPY3:{}   \tPY2:{},".format(self.count_alltarget, self.count_all3target, self.count_all2target))
        if self.count_alltarget:
            self.LogReport("  \t{}% converted\n".format(self.count_all3target*100/self.count_alltarget))

        return self.count_alltarget

    def ScanByFiles(self):
        print("not implemented")

    def CreateReport(self, scanType="target"):
        if scanType.lower() == "target":
            self.ScanByTarget()
        elif scanType.lower() == "file":
            self.ScanByFiles()
        else:
            raise ValueError("Scan type {} Not supported".format(scanType))
        return self.report

    def PrintReport(self):
        if self.report:
            print(self.report)

    def _ScanPyTestInContent(self, content):
        '''Find all the PY2 and PY3 test targets in the given content (from a BUILD file)

          parameters:
            content:  the BUILD file content
            return:   (PY3_target_list, PY2_target_list) in form of [ (target-type, name, PY2-or_PY3) ...]
        '''
        if content:
            pytest_sections = re.findall(self.pattern_pytest_section, content)    # [ (group), (group) ]
        
        py2tests = []
        py3tests = []
        for section in pytest_sections:
            found = re.findall(self.pattern_py2and3test, section)
            if found:
                target_type, name = found[0]
                py3tests.append((target_type, name, "2&3_test"))
                continue
            found = re.findall(self.pattern_pytest_py3, section)
            if found:
                target_type, name = found[0]
                py3tests.append((target_type, name, "PY3_test"))
                continue
            target_type, name = re.findall(self.pattern_pytarget_test, section)[0]
            py2tests.append((target_type, name, "P2_test"))

        return py3tests, py2tests

    def _ScanPyLibInContent(self, content):
        '''Find all the PY2 and PY3 lib targets in the given content (from a BUILD file)

          parameters:
            content:  the BUILD file content
            return:   (PY3_target_list, PY2_target_list) in form of [ (target-type, name, PY2-or_PY3) ...]
        '''
        if content:
            pylib_sections = re.findall(self.pattern_pylib_section, content)    # [ (group), (group) ]
        
        py2libs = []
        py3libs = []
        for section in pylib_sections:
            wholesection, target_type, name = section
            found = re.findall(self.pattern_srcver, wholesection)
            if found:
                srcver = found[0]
                if srcver in ("PY3", "PY2AND3"):
                    py3libs.append((target_type, name, "{}_lib".format(srcver)))
                else:
                    py2libs.append((target_type, name, "PY2_lib"))
                continue
            found = re.findall(self.pattern_pyver, wholesection)
            if found:
                pyver = found[0]
                if pyver == "PY3":
                    py3libs.append((target_type, name, "PY3_lib"))
                else:
                    py2libs.append((target_type, name, "PY2_lib"))
                continue
            py2libs.append((target_type, name, "P2_lib"))

        return py3libs, py2libs

    def _ScanPyBinInContent(self, content):
        '''Find all the PY2 and PY3 bin targets in the given content (from a BUILD file)

          parameters:
            content:  the BUILD file content
            return:   (PY3_target_list, PY2_target_list) in form of [ (target-type, name, PY2-or_PY3) ...]
        '''
        if content:
            pybin_sections = re.findall(self.pattern_pybin_section, content)    # [ (group), (group) ]
        
        py2bins = []
        py3bins = []
        for section in pybin_sections:
            wholesection, target_type, name = section
            found = re.findall(self.pattern_srcver, wholesection)
            if found:
                srcver = found[0]
                if srcver in ("PY3", "PY2AND3"):
                    py3bins.append((target_type, name, "{}_bin".format(srcver)))
                else:
                    py2bins.append((target_type, name, "PY2_bin"))
                continue
            found = re.findall(self.pattern_pyver, wholesection)
            if found:
                pyver = found[0]
                if pyver == "PY3":
                    py3bins.append((target_type, name, "PY3_bin"))
                else:
                    py2bins.append((target_type, name, "PY2_bin"))
                continue
            py2bins.append((target_type, name, "P2_bin"))

        return py3bins, py2bins


    def _PrintList(self, lst):
        if not lst or not isinstance(lst, list):
            return
        for item in lst:
            print("  {}".format(item))

    def LogReport(self, info):
        if isinstance(info, list) or isinstance(info, tuple):
            for x in info:
                self.report += "    {}\n".format(x)
        else:
            self.report += info


if __name__ == "__main__":

    arg_num = len(sys.argv)
    if arg_num ==2:
        rootdir = sys.argv[1]
        p3stat = Py3Stat(root_folder=rootdir)
        p3stat.CreateReport(scanType="target")
        p3stat.PrintReport()
    else:
        print("py2to3report.py <path-to-scan>")

    

