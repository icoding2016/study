"""
collections.OrderedDict
is a dict that can maintain the elements order

"""

from collections import OrderedDict


def printod(od:OrderedDict):
    print('OrderedDict {',end='')
    for k,v in od.items():
        print(f'{k}:{v} ', end='')
    print('}')

def test():
    print(dir(OrderedDict))
    od = OrderedDict()
    for i in range(10):
        od[i]=100+i
    printod(od)

    od[2]=1002
    printod(od)
    od.update({3:1003})
    printod(od)
    od.move_to_end(2)
    printod(od)
    od.popitem(last=False)
    printod(od)
    od.popitem()
    printod(od)
    od.pop(7)
    printod(od)



test()


