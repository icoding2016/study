# An array like [0,1,0,1,0,0,0,0,0] 
# 0 : you can walk, 1: you can not walk, otherwise you will die, 
# but if possible, you can skip that. Start :a[0], end:a[-1]
# Q: if that is possible to get a path from start to end if each time can skip or walk one step
# Improved question: each time can walk one step or skip [minj,maxj]step, if possible return one possible path

from call_counter import call_counter, show_call_counter


# T(2^w)  --  if 0(walk):2 options, for 1(skip) 1 option,  if 0 followed by 10 -> (2+1)*2. 
#             so if total w walk and s skip (s+w=n), the O(2^w+...)
@call_counter
def walk_skip(remain, min_skip, max_skip, cur_skip=0, path=None):
    if None == path:
        path = []
    if len(remain) == 0:
        yield path
        return
    if remain[0] == 0:  # walk
        if cur_skip < max_skip and cur_skip >= min_skip:
            for p in walk_skip(remain[1:], min_skip, max_skip, cur_skip+1, path+['s']):
                yield p
        for p in walk_skip(remain[1:], min_skip, max_skip, 0, path+['w']):
            yield p
    else:
        if cur_skip < max_skip and cur_skip >= min_skip:
            for p in walk_skip(remain[1:], min_skip, max_skip, cur_skip+1, path+['s']):
                yield p
    return


def walk_skip2(remain, min_skip, max_skip, cur_skip=0, path=None):
    if None == path:
        path = []
    if len(remain) == 0:
        print(path)
        return
    if remain[0] == 0:  # walk
        if cur_skip < max_skip and cur_skip >= min_skip:
            walk_skip2(remain[1:], min_skip, max_skip, cur_skip+1, path+['s'])
        walk_skip2(remain[1:], min_skip, max_skip, 0, path+['w'])
    else:
        if cur_skip < max_skip and cur_skip >= min_skip:
            walk_skip2(remain[1:], min_skip, max_skip, cur_skip+1, path+['s'])
    return


def test():
    #data = [0,1,0,1,0,0,0,0,0]
    data = [0,1,0,1,1,1,0,0,0]
    min_skip = 0
    max_skip = 3

    print('walk_skip:')
    for p in walk_skip(data, min_skip, max_skip):
        print(p)
    show_call_counter()

    print('walk_skip2:')
    walk_skip2(data, min_skip, max_skip)
    show_call_counter()

test()


