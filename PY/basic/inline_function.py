
def func1():
    L = [1,2,3,4]

    def inline_sublist(p,q):
        x = max(p, 0)
        y = min(q, len(L))     # use local varible 'L' in func1 directly
        return L[x:y+1]
    
    # test
    l1 = inline_sublist(1,2)
    print(l1)
    l2 = inline_sublist(1,3)
    print(l2)


if __name__ == "__main__":
    func1()

