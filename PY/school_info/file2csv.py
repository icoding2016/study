import csv
import os


DEBUG = True

def DebugLog(s):
    global DEBUG
    if (DEBUG):    print(s)

class File2Csv(object):
    def __init__(self, infn, outfn=None):
        assert(infn)

        self._input_file = os.path.abspath(infn)
        DebugLog("input file: {}".format(self._input_file))

        if not os.path.exists(infn):
            print(infn)
            raise ValueError("input file not exist: {}".format(infn))
        elif not os.path.isfile(infn):
            raise ValueError("input filename instead of dir: {}".format(infn))

        if outfn == None:          # default
            self._output_file = os.path.splitext(self._input_file)[0] + '.csv'
        else:
            if not os.path.exists(outfn):
                print("output file not exist: {}".format(outfn))
            elif os.path.isfile(infn):
                print("output filename instead of dir: {}".format(outfn))
            else:
                self._output_file = os.path.abspath(outfn)
        DebugLog("output file: {}".format(self._output_file))

    def OutputFileName(self):
        return self._output_file

    def run(self, delimeter=' ', grouplines = None):
        with open(self._output_file, 'w') as f_out:
            writer = csv.writer(f_out)
            with open(self._input_file, 'r') as f_in:
                curLineNum = 0
                curLine = ''
                sections = []
                if grouplines:
                    for line in f_in:
                        if curLineNum < grouplines:
                            sections.append(line)
                            curLineNum += 1
                        else:
                            writer.writerow(sections)
                            curLineNum = 1
                            sections.clear()
                            sections.append(line)

                else:
                    for line in f_in:
                        sections = line.split(delimeter)
                        writer.writerow(sections)
                        DebugLog('write row: {}'.format(sections))
    

def testFile2Csv(infn, outfn):
    f2c = File2Csv(infn, outfn)
    f2c.run(delimeter=" ", grouplines = 6)
    with open(f2c.OutputFileName(), 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)


if __name__ == '__main__':
    infn = '/usr/local/google/home/yanxie/code/study/PY/school_info/selective-order.txt'
    outfn = None
    testFile2Csv(infn, outfn)

