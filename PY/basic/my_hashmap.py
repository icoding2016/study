# to implement a hashmap
# The hashmap support add(key, value), get(key), del() in O(1),
# also support some other method like len(), str()
# 
#  
# Keys:
#   How to map the key to an index (0 ~ bucket_num)?
#   hash alghorithm options. 
#     -  sum(ascii of chars) % bucket_num         --> sum([ord(c) for c in s]) % bucket_num
# 
# 
# 
#  
#  





import json
from typing import Hashable, TypeVar, Optional


T = TypeVar('T')



def hash_chrsum(key:Hashable, bucket_num:int) -> int:
    if isinstance(key, int):
        return key % bucket_num
    keystr = json.dumps(key)
    keysum = 0
    for c in keystr:
        keysum += ord(c)
    return keysum % bucket_num


class MyHashMapError(Exception):
    pass


class MyHashMap(object):
    DEF_BUCKET_NUM = 10
    hash_methods = {
        'chrsum': hash_chrsum,
    }

    def __init__(self, bucket_num:int=0, hash_method:str='chrsum') -> None:
        super().__init__()
        self._bucket_num = bucket_num if bucket_num else MyHashMap.DEF_BUCKET_NUM
        self._buckets = [None for _ in range(self._bucket_num)]
        if not hash_method in MyHashMap.hash_methods:
            raise MyHashMapError(f'Unknown hash method: {hash_method}')
        self.hash_method = MyHashMap.hash_methods[hash_method]

    def _hash(self, key:Hashable) -> int:
        """" To hash the key into the index of buckets """
        return self.hash_method(key, self._bucket_num)

    def add(self, key:Hashable, value:T) -> None:
        index = self._hash(key)
        if not self._buckets[index]:
            self._buckets[index] = [(key, value)]
        else:
            self._buckets[index].append((key, value))

    def get(self, key:Hashable) -> Optional[T]:
        index = self._hash(key)
        if not self._buckets[index]:
            return None
        for k,v in self._buckets[index]:
            if k == key:
                return v
        return None

    def delete(self, key:Hashable) -> bool:
        index = self._hash(key)
        if not self._buckets[index]:
            return False
        for k,v in self._buckets[index]:
            if k == key:
                del self._buckets[index][key]
                return True
        return False

    def __len__(self) -> int:
        count = 0
        for i in range(self._bucket_num):
            if not self._buckets[i]:
                continue
            count += len(self._buckets[i])
        return count

    def __str__(self) -> str:
        s = '{'
        for index in range(self._bucket_num):
            if not self._buckets[index]:
                continue
            for i, (k, v) in enumerate(self._buckets[index]):
                s += f'{k}:{v}'
                if i < len(self._buckets[index]-1):
                    s += ', '
            if index < len(self._bucket_num) - 1:
                s += ','
        s += '}'
        return s

    def debug(self):
        for index in range(self._bucket_num):
            print(f'Bucket {index}: ', end='')
            if not self._buckets[index]:
                print('None')
            else:               
                for i, (k, v) in enumerate(self._buckets[index]):
                    print(f'{k}:{v}', end=',')
                    if i == len(self._buckets[index])-1:
                        print('')
                if index == self._bucket_num-1:
                    print('')



def test():
    data = {'Jenny':12, 'John':25, 'Ann':27, 'Emily':16, 'Peter':24, 'Jerry':32, 'Julian':18, 'Stan':12, 
            1527:36, ('ET','Alien'):245}
    hashmap = MyHashMap()
    for k, v in data.items():
        hashmap.add(k, v)
    print(len(hashmap), len(data))
    hashmap.debug()


test()
