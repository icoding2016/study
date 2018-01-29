from __future__ import print_function

import random

class everyday_exec(object):
    def __init__(self):
        self.genCombinitionSet()
        self.linewidth = 8

    # return a set of number-pairs
    def genCombinitionSet(self):
        self._combSet_add = []
        numSet = [i for i in range(1, 10)]
        for i in numSet:
            for j in numSet:
                if (i, j) in self._combSet_add or (j, i) in self._combSet_add:
                    continue
                else:
                    self._combSet_add.append((i, j))
        print("CombinitionSet_adding generated: {}\n".format(self._combSet_add))

        # gen times set
        self._combSet_times = []
        numSet = [x for x in range(1, 10)]
        random.shuffle(numSet)
        while len(numSet):
            i = numSet.pop()
            if len(numSet) != 0:
                j = numSet.pop()
            else:
                j = i
            for k in range(2, 10):
                self._combSet_times.append((i,j,k))
        print("CombinitionSet_times generated ({}): {}\n".format(len(self._combSet_times), self._combSet_times))

        # gen times set
        self._combSet_div = []
        for i in range(3,10):
            for j in range(3,10):
                if (i, j) in self._combSet_div or (j, i) in self._combSet_div:
                    continue
                self._combSet_div.append((i,j))
        #random.shuffle(self._combSet_div)
        print("CombinitionSet_div generated ({}): {}\n".format(len(self._combSet_div), self._combSet_div))

    def genAddingSet(self):
        addingSet = []
        s = self._combSet_add.copy()
        random.shuffle(s)
        while len(s):
            pair1 = s.pop()
            if len(s):
                pair2 = s.pop()
            else:
                pair2 = pair1
            num1 = pair1[0] * 10 + pair2[0]
            num2 = pair1[1] * 10 + pair2[1]
            addingSet.append((num1, num2))
        #print("AddSet generated ({}): {}".format(len(addingSet), addingSet))
        return addingSet

    def genSubstractSet(self):
        abstractSet = []
        count = 0
        while count < 24:
            x = random.randint(1,99)
            y = random.randint(1,99)
            if x == y:
                continue
            if x < y:
                x, y = y, x
            if x < 10 or y < 10:
                continue
            abstractSet.append((x, y))
            count += 1
        return abstractSet

    def genTimesSet(self):
        timesSet = []
        s = self._combSet_times.copy()
        random.shuffle(s)
        while len(s):
            i, j, k = s.pop()
            timesSet.append((i*10+j, k))
        return timesSet

    def genDivSet(self):
        divSet = []
        s = self._combSet_div.copy()
        random.shuffle(s)
        while len(s):
            i, j = s.pop()
            divSet.append((i*j, i))
            if i != j:
                divSet.append((i * j, j))
        random.shuffle(divSet)
        return divSet


    def shuffle(self, l):
        random.shuffle(l)
        print(l)

    def addingExec(self):
        aset = self.genAddingSet()
        print("Add [{}]:".format(len(aset)))
        count=0
        for x, y in aset:
            print("{}+{}=__".format(x, y), end="\t")
            count+=1
            if count >= 6:
                #print("")
                count = 0

    def substractExec(self):
        sset = self.genSubstractSet()
        print("Sub [{}]:".format(len(sset)))
        count=0
        for x, y in sset:
            print("{}-{}=__".format(x, y), end="\t")
            count+=1
            if count >= 6:
                #print("")
                count = 0

    def timesExec(self):
        tset = self.genTimesSet()
        random.shuffle(tset)
        print("Time[{}]:".format(len(tset)))
        count = 0
        for x, y in tset:
            print("{}x{}=__ ".format(x, y), end="\t")
            count += 1
            if count >= 5:
                #print("")
                count = 0

    def genQuiz(self):
        a = self.genAddingSet() + self.genAddingSet()
        #print("generate add-set[{}]".format(len(a)))
        s = self.genSubstractSet() + self.genSubstractSet()
        #print("generate sub-set[{}]".format(len(s)))
        t = self.genTimesSet()
        #print("generate time-set[{}]".format(len(t)))
        d = self.genDivSet()
        #print("generate div-set[{}]".format(len(d)))
        self.output_quiz(a, s, t, d)

    def output_quiz(self, a, s, t, d):
        linewidth = self.linewidth
        line = 0
        count = 0
        m = min([len(a), len(s), len(t), len(d)])
        while line < int(m/linewidth):
            for i in range(linewidth):
                x,y = a[count+i]
                print("{}+{}=__".format(x, y), end="\t")
            print('')
            for i in range(linewidth):
                x,y = s[count+i]
                print("{}-{}=__".format(x, y), end="\t")
            print('')
            for i in range(linewidth):
                x, y = t[count + i]
                print("{}x{}=__ ".format(x, y), end="\t")
            print('')
            for i in range(linewidth):
                x, y = d[count + i]
                print("{}/{}=__ ".format(x, y), end="\t")
            print('')
            print('-' * 68)
            count += linewidth
            line += 1

    def genQuiz_old(self):
        repeat = 3
        for i in range(repeat):
            self.addingExec()
            print('\n' + '-' * 90)
            self.substractExec()
            print('\n' + '-' * 90)
            self.timesExec()
            print('\n' + '-' * 90)

    def go(self):
        repeat = 5
        for i in range(repeat):
            self.genQuiz()

    def timeTable(self):
        tab = ["Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve"]
        for i in range(0, len(tab)):
            print("{}".format(tab[i]) , end="\t|\t")
        for i in range(0, 13):
            for j in range(0, 13):
                x = i * j
                print("{}x{}={}".format(j, i, x), end='\t|\t')
            print("")

if __name__ == "__main__":
    math1 = everyday_exec()
    math1.go()
    #math1.timeTable()




