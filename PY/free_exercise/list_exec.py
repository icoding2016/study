# Quesitons
# 1.  A array contains the number(1~n), the len(a)=n
#     There are one missing number and one repeated number
#     Find out the missing and repeated ones




def find_duplicate(a:list[int]) -> int:
    d = {}
    for x in a:
        if x in d:
            return x
        else:
            d[x] = 1
    return None

def find_missing(a:list[int]) -> int:
    return sum([x for x in range(1, len(a)+1)]) - sum(set(a))




def test():
    A = [1,2,3,4,5,6,7,8,9,10]
    A1 = [1,2,3,8,5,6,7,8,9,10]
    A2 = [10,2,3,4,5,6,7,8,9,10]
    print(find_duplicate(A1))
    print(find_missing(A1))
    print(find_duplicate(A2))
    print(find_missing(A2))    

test()
