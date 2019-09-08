DEBUG = 1

def Debug(s):
    global DEBUG
    if (DEBUG):
        print(s)


def S(N):
    b = str(bin(N))[2:]
    max_len = 0
    cur_len = 0
    pairing = False
    found_pair = False
    l = len(b)

    Debug("{} - {}".format(N,b))

    if len(b) < 3:
        return 0

    for i in range(len(b)):
        if b[i] == '1' and not pairing:    #  1x, start pairing
            cur_len = 0
            pairing = True
            Debug("{}: start pairing".format(b[i]))
        elif b[i] == '1' and pairing:     #  1x or 11x
            if cur_len == 0:            #  11x
                Debug("{}: continue 1 to start pairing".format(b[i]))
                continue
            else:   # end of current pairing
                if cur_len > max_len:    max_len = cur_len
                Debug("{}: end pairing. cur_len={}".format(b[i], cur_len))
                pairing = False
                cur_len = 0
                found_pair = True
        elif b[i] == '0' and not pairing:   #  00x
            Debug("{}: 0 without pairing".format(b[i]))
            continue
        elif b[i] == '0' and pairing:       #  10
            Debug("{}: 0 within pairing".format(b[i]))
            cur_len += 1
        else:
            print("WRONG")
    if not found_pair:
        return 0
    return max_len


if __name__ == "__main__":

    sample = [
        9,
        529,
        20,
        15,
        32
    ]

    for x in sample:
        r = S(x)
        print("{} -> {}".format(x, r))

