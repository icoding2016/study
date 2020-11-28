# Input a set of country name ,population, 
# Implement a class for getRandomCountry, based on the population percentage

import collections
import random

class RandomCountry(object):
    def __init__(self, data:set[tuple])->None:
        self.data = data
        self.scale = []
        self.portion = {}
        self.total = 0
        self.init_data()
    
    def init_data(self):
        if not self.data:
            return
        self.total = 0
        for n, p in self.data:
            self.total += p
            self.scale.append((n, self.total))

        for n, p in self.data:
            self.portion[n] = p/self.total

    def get_random_country(self)->str:
        rand = random.randint(0, self.total)
        for i in range(len(self.scale)):
            if self.scale[i][1] > rand:
                return self.scale[i][0]
        raise Exception()

    def portion_info(self):
        s = ''
        for n,p in self.portion.items():
            s = s + '{}:{:.1f}%, '.format(n,p*100)
        return s

def test():
    data = [('Australia', 25000000), ('China', 1400000000), ('USA', 300000000), ('Italy', 20000000), ('Span', 30000000), ('Indian', 1000000000),]
    rc = RandomCountry(data)
    n = 500
    result = [rc.get_random_country() for i in range(n)]
    #print(result)
    print(collections.Counter(result))
    print('expection: ', rc.portion_info())

test()