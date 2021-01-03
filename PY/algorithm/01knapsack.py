# 0-1 Knapsack Problem | DP-10
# Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. 
# In other words, given two integer arrays val[0..n-1] and wt[0..n-1] which represent values and weights associated with n items respectively. 
# Also given an integer W which represents knapsack capacity, 
# find out the maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to W. 
# You cannot break an item, either pick the complete item or don’t pick it (0-1 property).
#
# Solution 1: Recursive
#   Recursively pick remain values from the value list and check if meet condition
#   con:  many duplicates, or to deal with duplicates
#   
# Solution 2:
#   Every value has 2 options, select (1) or no-select (0). so iterate all possibilties.  that is a 2^n.
#   use DP memo to optimize     


from call_counter import call_counter, show_call_counter


# Recursive, count only
# T(2^N) ?
# S(N)
@call_counter
def knapsack_count(values:list, weights:list, cap:int, cur_value:int=0, best:int=0)->int:
    if len(values) == 0 or cap < min(weights):
        #v, _ = calculate_vw(values, weights, selected)
        if cur_value > best:
            best = cur_value
        return best

    if cap-weights[0] >= 0:
        best = knapsack_count(values[1:], weights[1:], cap-weights[0],  cur_value + values[0], best)
    best = knapsack_count(values[1:], weights[1:], cap, cur_value, best)
    return best


# Use selected to record current selection. to reduce duplicate (but still duplicates)
# note: this isn't a good implementation.. it use permutation not combination.
#   'for i in range(len(values))' needed when order matters. but this is not the case.
#   combination care about choose/no-choose for each element.  
@call_counter
def knapsack_recursive(values:list, weights:list, cap:int, cur_selection:list=None, best:dict[int:list]=None)->(int,dict):
    if None == best:
        best = {'v':0, 's':[]}    # { 'v':<value>, 's':[] }
    if None == cur_selection:
        cur_selection = [0] * len(values)    # 

    v, _ = calculate_vw(values, weights, cur_selection)
    remain_weights = [weights[i] for i in cur_selection if i == 0]

    if 0 not in cur_selection or (cap >= 0 and cap < min(remain_weights)):
        if v > best['v']:
            best['v'] = v
            best['s'] = cur_selection
            return v, best
        else:
            #print('skip plan:', v, cur_selection)
            return best['v'], best
    
    total = 0
    for i in range(len(values)):
        if cur_selection[i] == 1:
            continue
        cs = cur_selection.copy()
        cs[i] = 1
        if cap - weights[i] >= 0:
            total, _ = knapsack_recursive(values, weights, cap-weights[i], cs, best)
        cs = None
    return total, best
    

def calculate_vw(values:list, weights:list, selection:list) -> (int,int):
    v = 0
    w = 0
    for i in range(len(selection)):
        if selection[i]:
            v += values[i]
            w += weights[i]
    return v, w


# use bitmap, if the number is not big.  n < digit_len(int)
@call_counter
def knapsack_bitmap(values:list, weights:list, cap:int)->(int,dict):
    #best = {'v':}
    best_value = 0
    best_map = ''
    for i in range(2**len(values)):
        v, w = get_vw_from_bitmap(values, weights, i)
        if w > cap:
            continue
        if v > best_value:
            best_value = v
            best_map = '{:b}'.format(i)
        #print(v, '{:b}'.format(i))
    return best_value, best_map

def get_vw_from_bitmap(values:list, weights:list, selection_map:int)->(int, int):
    v = 0
    w = 0
    for i in range(len(values)):
        if selection_map & (1<<i):
            v += values[i]
            w += weights[i]
    return v,w



def test():
    V = [60, 100, 120, 40, 30]
    W = [10, 20, 30, 5, 3]
    C = 50

    print("knapsack_count")
    print(knapsack_count(V, W, C))
    show_call_counter()

    print("knapsack_recursive")
    print(knapsack_recursive(V, W, C))
    show_call_counter()

    print("knapsack_bitmap")
    print(knapsack_bitmap(V, W, C))
    show_call_counter()

test()