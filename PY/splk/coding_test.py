# 给定一个数组，元素有正有负，找到第一个元素的位置i使得[0:i)和(i:len-1]的和相等，
# 即如果该数字左边所有的元素的和等于该数字邮编所有元素的和，那么就返回该数字的下标，
# 如果没有这样的可以做分隔的数字，就返回-1， 
# 例如[1,2,3,4,8,5,5]就返回坐标=4（数字8的位置）
# 这个题本身很简单，问了很多关于这道题如何设计test cases去测performance的问题
# 描述一下时间空间复杂度。
# 我还自己提出是否有优化的方法，然后自己又否决了binary search优化，因为元素里有负数。
# 
# 
# Idea:
#   - Prepare data:  go through the data list from both left-> and right<-, calculate the left_sum , right_sum at i
#     option 1: rec[i]: sum(data[0:i]), sum(data[i+1:]) 
#     option 2: rec[i]: rec[i-1]+data[i-1], rec[i+1]+data[i+1]
#   - find i where left_sum[i] = right_sum[i]
#  


from utils.testtools import test_fixture


class Solution():

    # DP solution
    # O(N)
    def findMiddle(self, data:int) -> int:
        if len(data) < 3:
            return -1
        sum_rec = [[None,None] for i in range(len(data))]   # rec[i]=[sum_l, sum_r]
        sum_rec[0][0] = 0
        sum_rec[1][0] = data[0]
        sum_rec[-1][1] = 0
        sum_rec[-2][1] = data[-1]
        for i, v in enumerate(data):
            if i > 1:
                sum_rec[i][0] = sum_rec[i-1][0] + data[i-1]
            j = len(data)-1-i
            if j < len(data)-2:
                sum_rec[j][1] = sum_rec[j+1][1] + data[j+1]
        for i in range(len(sum_rec)):
            if sum_rec[i][0] == sum_rec[i][1]:
                return i
        return -1       


def test_findMiddle():
    print('test_findMiddle')
    data = [
        (([1],), -1),
        (([1,2],), -1),
        (([3,1,3],), 1),
        (([1,2,3,4,8,5,5],), 4),
        (([2,-1,3,0,4,-1,1,-3,0],), 2),
        (([2,-1,3,0,4,-1,1,-2,0],), -1),
    ]
    s = Solution()
    test_fixture(s.findMiddle, data)


def test():
    test_findMiddle()


test()
