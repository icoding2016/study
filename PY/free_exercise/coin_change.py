# Algorithm for finding the different ways of making change for a given amount using a specified set of coin denominations.
# Say we have 50c,20c,10c,5c,1c coins,  how can we make change of changes (e.g changes=34)
# There are some typical questions:
#   1) unlimited coins, what is the possible combinations
#   2) limited coins, what are the possible combinations
#   3) what is the solution for the fewest coin number 
#

from functools import reduce
from call_counter import call_counter, show_call_counter

COINS = [50,20,10,5,1]


# solution with duplications
# T(N^Changes)    for each round there are N (type of coins) options, max Change level. So N+N*N+...N^change
# S(Changes)
@call_counter
def coin_change_iter_dup(changes:int, cur:int=0, selected:dict=None) -> None:
    global COINS
    if None == selected:
        selected = {50:0, 20:0, 10:0, 5:0, 1:0}
    
    if cur == changes:
        yield selected
        return

    for c in COINS:
        if changes - cur >= c:
            s = selected.copy()
            s[c] += 1
            for s in coin_change_iter_dup(changes, cur+c, s):
                yield s

# Solution with memorizing
# T()
@call_counter
def coin_change_memo(changes:int, cur:int=0, selected:dict=None, memo:list=None)->list:
    global COINS
    if None == selected:
        selected = {50:0, 20:0, 10:0, 5:0, 1:0}
    if None == memo:
        memo = []
    if changes == cur:
        if selected not in memo:
            memo.append(selected)
        return memo
    for c in COINS:
        if c + cur <= changes:
            s = selected.copy()
            s[c] += 1
            if s in memo:
                continue
            coin_change_memo(changes, cur+c, s, memo)
    return memo


# solution with no duplications
@call_counter
def coin_change_iter(coins:list, changes:int, cur:int=0, selected:dict=None) -> None:
    if None == selected:
        selected = {50:0, 20:0, 10:0, 5:0, 1:0}
    
    if cur == changes:
        yield selected
        return
    if cur > changes:
        return
    if not coins:
        return

    c = coins[0]
    s = selected.copy()
    s[c] += 1
    for x in coin_change_iter(coins[:], changes, cur+c, s):
        yield x
    for x in coin_change_iter(coins[1:], changes, cur, selected):
        yield x

@call_counter
def coin_change_iter2(coins:list, changes:int, selected:dict=None) -> None:
    if None == selected:
        selected = {50:0, 20:0, 10:0, 5:0, 1:0}
    
    cur = reduce(lambda x,y:x+y, [v*c for (v,c) in selected.items()])
    if cur == changes:
        yield selected
        return
    if cur > changes:
        return
    if not coins:
        return

    c = coins[0]
    s = selected.copy()
    s[c] += 1
    for x in coin_change_iter2(coins[:], changes, s):
        yield x
    for x in coin_change_iter2(coins[1:], changes,  selected):
        yield x



def change(n, coins_available, coins_so_far):
	if sum(coins_so_far) == n:
		yield coins_so_far
	elif sum(coins_so_far) > n:
		pass
	elif coins_available == []:
		pass
	else:
		for c in change(n, coins_available[:], coins_so_far+[coins_available[0]]):
			yield c
		for c in change(n, coins_available[1:], coins_so_far):
			yield c


def 


def test():
    changes = 11

    print('coin_change_iter_dup')
    for x in coin_change_iter_dup(changes):
        print(x)
    #coin_change_iter_dup(changes)
    show_call_counter()

    print('coin_change_memo')
    print(coin_change_memo(changes))
    show_call_counter()

    print('coin_change_iter')
    for x in coin_change_iter(COINS[:], changes):
        print(x)
    show_call_counter()

    print('coin_change_iter2')
    for x in coin_change_iter2(COINS[:], changes):
        print(x)
    show_call_counter()


    print('change')
    for x in change(changes, COINS[:], []):
        print(x)
    show_call_counter()


test()    