# Print all positive integer solutions to the equation a^3 + b^3 = C^3 + d^3 
# where a, b, c, and d are integers between 1 and 1000
#
# solution1: brutal force, 4 loops.   O(N^4)
#
# solution2: d = pow(a^3 + b^3 - c^3, 1/3),   O(N^3)
#
# solution3: cache the (x,y) pair result (x^3+y^3) in hash table.  there may be some results have multiple (x,y) pairs
#

scope=1000

def solution1(scope):
    answer=[]
    for a in range(1, scope+1):
        for b in range(1, scope+1):
            for c in range(1, scope+1):
                for d in range(1, scope+1):
                    if a*a*a + b*b*b == c*c*c + d*d*d:
                        answer.append([a,b,c,d])
    print(answer)
    return answer

def solution2(scope):
    answer=[]
    for a in range(1, scope+1):
        for b in range(1, scope+1):
            for c in range(1, scope+1):
                d = int(pow(a*a*a + b*b*b - c*c*c, 1/3))  # round off to int
                if a*a*a + b*b*b == c*c*c + d*d*d:
                    answer.append([a,b,c,d])
    print(answer)
    return answer


def solution3(scope):
    answer = []
    results = {}        # result:[(x,y) pairs]
    for a in range(1, scope+1):
        for b in range(1, scope+1):
            result = a*a*a + b*b*b
            if not result in results:
                results[result] = [(a, b)]
            else:
                results[result].append((a, b))

    for result in results:
        if len(results[result]) > 1:
            for i in range(len(results[result])-1):
                for j in range(i, len(results[result])):
                    answer.append(results[result][i] + results[result][j])

    print(answer)
    return answer


if __name__ == '__main__':
    S = 20
    solution1(S)
    print('-'*80)
    solution2(S)
    print('-'*80)
    solution3(S)
