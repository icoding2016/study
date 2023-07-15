"""
itertools

itertools.
  .count()          count(10) --> 10 11 12 13 14 ...
  .cycle():         cycle('ABCD') --> A B C D A B C D ...
  .repeat():        repeat(10, 3) --> 10 10 10
  .accoumulate():   accumulate([1,2,3,4,5]) --> 1 3 6 10 15
  .compress('ABCDE', [1, 0, 1, 0, 0]):   A C
  .islice(iterable, start, stop, step):  eg. islice(range(20), 2, 10, 2): [2,4,6,8]  (2 is the start 'value', 10 the end 'value' not inclusive)   # 
  .dropwhile(func, seq):

  .product('ABCD', repeat=2): AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
  .permutations('ABCD', 2):   AB AC AD BA BC BD CA CB CD DA DB DC
  .combinations('ABCD', 2):   AB AC AD BC BD CD
  .combinations_with_replacement('ABCD', 2): AA AB AC AD BB BC BD CC CD DD

"""

from itertools import count, takewhile, permutations, product, islice, dropwhile

def range_float(start:float, stop:float, step:float):
    gen = takewhile(lambda x:x<stop, count(start, step))
    return list(gen)

print(range_float(1.2, 2.1, 0.2))

def kth_permutation(numbers, k):
    return list(permutations(numbers, len(numbers)))[k-1]

print(f"kth_permutation: {kth_permutation('1234', 3)}")

# p = product([1,2,3,4], repeat=2)
print(f"product: {[p for p in product([1,2,3,4], repeat=2)]}")

print(f"islice(range(20), 2, 10, 2): {[x for x in islice(range(20), 2, 10, 2)]}")

exp = "list(dropwhile(lambda x:x<0, [-3, -8, -6, 9, 4, -1, 7]))"
print(f"{exp} -> {eval(exp)}")

