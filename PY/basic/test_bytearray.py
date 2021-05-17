

def in_place_modify(s:str):
    ba = bytearray(s, encoding='utf-8')

    print(id(ba), ba, ' --> ', end='')

    for i in range(len(ba)):
        ba[i] = ba[i] - 32
    print(ba)
    print(id(ba), ba.decode())


in_place_modify('abcd')


