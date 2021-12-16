# Given a CSV, how would you generate counts of unique IP addresses across rows?
#
# 
#  n1.n2.n3.n4
#  rule:  
#  - 0<=n<255
#  - exceptions:  [127.0.0.1, 224.0.0.0~239.255.255.255, ..] 
# 
# 
# 
#  


import random


class InvalidIp(Exception):
    pass


class IpCreator(object):
    IP_EXCLUDE = ['127.0.0.1', '']

    def __init__(self):
        pass

    @classmethod
    def is_excluded_ip_str(cls, ip:str) -> bool:
        if ip in cls.IP_EXCLUDE:
            return True
        # exclude multicast
        sections = ip.split('.')
        n1 = int(sections[0])
        if 224 <= n1 <= 239:
            return True
        return False

    @classmethod
    def is_excluded_ip(cls, ip:tuple[int]) -> bool:
        if len(ip) != 4:
            raise InvalidIp(f'Invalid IP {ip}')
        if '.'.join(str(ip)) in cls.IP_EXCLUDE or 224 <= ip[0] <=239:
            return True
        return False

    @classmethod
    def create(cls, count:int) -> set[tuple[int]]:
        result = set()
        while len(result) < count:
            ip = cls.new_ip()
            if not cls.is_excluded_ip(ip):
                result.add(ip)
        return result
    
    @classmethod
    def new_ip_str(cls) -> str:
        sections = []
        for i in range(4):
            num = random.randint(0, 254)
            sections.append(str(num))
        return '.'.join(sections)

    @classmethod
    def new_ip(cls) -> tuple[int]:
        sections = []
        for i in range(4):
            num = random.randint(0, 254)
            sections.append(num)
        return tuple([n for n in sections])

    @classmethod
    def gen_ip(cls) -> tuple[int]:
        sections = []
        while True:
            for i in range(4):
                num = random.randint(0,254)
                sections.append(num)
            ip = tuple([n for n in sections])
            yield ip
            sections.clear()

    @classmethod
    def get_ip(cls) -> tuple[int]:
        return next(cls.gen_ip())


def test():
    ipc = IpCreator()
    ips = ipc.create(10)
    for ip in ips:
        print('.'.join([str(s) for s in ip]))

    print('generator')
    count = 0
    # for ip in ipc.get_ip():    # endless loop
        # if count >= 10:
        #     break
        # print('.'.join([str(s) for s in ip]))
    for i in range(5):
        print(next(ipc.gen_ip()))

    print('get_ip')
    for i in range(5):
        print(ipc.get_ip())

test()
