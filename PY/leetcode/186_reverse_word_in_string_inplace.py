"""
186. Reverse Words in a String II
Medium

https://leetcode.ca/all/186.html


Given an input string , reverse the string word by word. 

Example:
Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]

Note: 
    A word is defined as a sequence of non-space characters.
    The input string does not contain leading or trailing spaces.
    The words are always separated by a single space.

Follow up: Could you do it in-place without allocating extra space?


"""


from typing import List


# use extra space.
# T(N)
def reverse_words_extraspace(wl:List[str]) -> List[str]:
    words = ''.join(wl).split(' ')
    rwords = reversed(words)
    return [x for x in ' '.join(rwords)]


# in-place
# idea:  bubble up and bubble down the whole word from both direction
def reverse_words(wl:List[str]) -> List[str]:
    N = len(wl)
    p1, p2 = 0, N -1
    while p1 <= p2:
        for i in range(p1, p2):
            print("one", p1, p2)
            if wl[i] != ' ':
                continue
            else:
                print(f"i={i}")
                word_len = i - p1
                rotate_r(wl, p1, word_len+1, 1)
                print(wl)
                bubble_word_right(wl, p1, word_len+1, p2)
                print(wl)
                # p1 += word_len + 1
                p2 -= word_len + 1
        if p1 <= p2:
            break
        print("two", p1, p2)
        for i in range(p2, p1, -1):
            if wl[i] != ' ':
                continue
            else:
                word_len = p2 - i
                rotate_l(wl, i, word_len+1, 1)
                print(f"i={i}")
                print(wl)
                bubble_word_left(wl, i, word_len+1, p1) 
                print(wl)
                # p2 -= word_len + 1
                p1 += word_len + 1
    return 

def swap_section(arr:List[str], p1:int, p2:int, length:int):
    for i in range(length):
        arr[p1+i], arr[p2+i] = arr[p2+i], arr[p1+i] 

# word rotate right n steps
def rotate_r(arr:List[str], pos:int, length:int, step:int):
    for i in range(step):
        for r in range(length-1):
            arr[pos+length-r-2], arr[pos+length-r-1] = arr[pos+length-r-1], arr[pos+length-r-2]

def rotate_l(arr:List[str], pos:int, length:int, step:int):
    for i in range(step):
        for r in range(length-1):
            arr[pos+length-r-2], arr[pos+length-r-1] = arr[pos+length-r-1], arr[pos+length-r-2]


def bubble_word_right(arr:List[str], pos:int, length:int, right:int):
    for i in range(length-1, -1, -1):
        for j in range(right-pos-length+1):
            arr[pos+i+j], arr[pos+i+j+1] = arr[pos+i+1+j], arr[pos+i+j]

def bubble_word_left(arr:List[str], pos:int, length:int, left:int):
    for i in range(length):
        for j in range(pos-left):
            arr[pos+i-j], arr[pos+i-1-j] = arr[pos+i-1-j], arr[pos+i-j]




def test_swap_section():
    arr = [c for c in '1234567890']
    swap_section(arr, 1, 7, 3)
    print(arr)

def test_rotate_r():
    arr = [c for c in '1234567890']
    rotate_r(arr, 1, 4, 2)
    print("rotate_r", arr)

def test_rotate_l():
    arr = [c for c in '1234567890']
    rotate_l(arr, 1, 5, 2)
    print("rotate_l", arr)

def test_bubble_word_right():
    arr = [c for c in '1234567890']
    bubble_word_right(arr, 1, 3, 9)
    print(arr)

def test_bubble_word_left():
    arr = [c for c in '1234567890']
    bubble_word_left(arr, 5, 4, 1)
    print(arr)


test_data = [
    ((["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"],), ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]),
]


def test():
    for a, e in test_data:
        # r = reverse_words_extraspace(*a)
        r = reverse_words(*a)
        print(f"result: {a[0]}")
        if e == r:
            print('Pass')
        else:
            print(f"expect: {e}")
            print('Fail')


# test_swap_section()
# test_rotate_r()
# test_rotate_l()
# test_bubble_word_right()
# test_bubble_word_left()
test()
