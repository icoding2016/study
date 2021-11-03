# serializing data
# https://docs.python-guide.org/scenarios/serialization/

import pickle
import json



class Test(object):
    def __init__(self, url:str, result:bool, errcode:int, rsptime:int) -> None:
        self.url = url           
        self.result = result     
        self.errcode = errcode   
        self.rsptime = rsptime   

    def d(self):
        return {
           'url':self.url,
           'result':self.result,
           'errcode':self.errcode,
           'resptime':self.rsptime
        }



def test():
    t = Test('http://some.url.com', True, 0, 30)

    d = t.d()
    print(d)
    #print(bytes(d))

    b = pickle.dumps(d)
    print(b)        
    print(str(b))

    o = pickle.loads(b)
    print(o)
    print(type(o))


test()
