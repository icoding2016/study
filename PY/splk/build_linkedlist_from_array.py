# Splunk OA
#  
# the first node (the head) islocated at index 0;
# A non-empty array A consisting of N integers is given. 
# Array A represents a linked-list.  
# A list is constructed from this array as follows:
# - the first node (the head) islocated at index 0;
# - if the value of a node is -1 then it is the last node of the list;
#   otherwise the successor of a node located at index k is located at indexA[K] (you can assume that A[k] is a valid index that is 1<=A[k]<N) 
# For example for array A such that: A[0]=1,A[1]=4,A[2]=-1,A[3]=3,A[4]=2,
# the following list is constructed: 1 -> 4 -> 2 -> -1
#   the first node (the head) is located at index0 and has a value of 1;
#   the second  node is located at index1 and has a value of 4;
#   the third node is located at index4 and has a value of 2;
#   the fourth node is located at index2 and has a value of -1
#
# Write a function: class Solution { public int solution(int[]A);}
# That give a non-empty array A consisting of N integers
# returns the length of the list constructed from A in the above manner
# 
# 
# 
#  


from utils.testtools import test_fixture


class InvalidInput(Exception):
    pass

class Solution():
    def buildLinkedList(self, data:list[int]) -> int:
        if not data:
            return 0
        if -1 not in data:
            raise InvalidInput('The input array should contain -1')
        value = data[0]
        count = 1
        while value != -1:
            count += 1
            value = data[value]
        return count


def test():
    data = [
        (([-1], ), 1),
        (([1, -1], ), 2),
        (([1,4,-1,3,2], ), 4),
        # ((, ), ),
        # ((, ), ),
    ]

    s = Solution()
    test_fixture(s.buildLinkedList, data)

test()
