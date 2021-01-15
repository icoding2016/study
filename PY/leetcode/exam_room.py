# In an exam room, there are N seats in a single row, numbered 0, 1, 2, ..., N-1.
# When a student enters the room, they must sit in the seat that maximizes the distance to the closest person.  
# If there are multiple such seats, they sit in the seat with the lowest number.  
# (Also, if no one is in the room, then the student sits at seat number 0.)
# Return a class ExamRoom(int N) that exposes two functions: ExamRoom.seat() returning an int representing what seat the student sat in, 
# and ExamRoom.leave(int p) representing that the student in seat number p now leaves the room.  
# It is guaranteed that any calls to ExamRoom.leave(p) have a student sitting in seat p.

 

# Example 1:

# Input: ["ExamRoom","seat","seat","seat","seat","leave","seat"], [[10],[],[],[],[],[4],[]]
# Output: [null,0,9,4,2,null,5]
# Explanation:
# ExamRoom(10) -> null
# seat() -> 0, no one is in the room, then the student sits at seat number 0.
# seat() -> 9, the student sits at the last seat number 9.
# seat() -> 4, the student sits at the last seat number 4.
# seat() -> 2, the student sits at the last seat number 2.
# leave(4) -> null
# seat() -> 5, the student sits at the last seat number 5.
# ​​​​​​​
# Note:
# 1 <= N <= 10^9
# ExamRoom.seat() and ExamRoom.leave() will be called at most 10^4 times across all test cases.
# Calls to ExamRoom.leave(p) are guaranteed to have a student currently sitting in seat number p.
#
# Ideas:
#   Solution:
#     keep the occupied seats number in ascending order,  calculate the greatest gap 
#     T(N)
#     S(N)
#   Below answer still has issue. cannot pass test.  https://leetcode.com/problems/exam-room/    icoding2016
#   

class ExamRoom(object):
    def __init__(self, N: int):
        self.seat_num = N
        self.sit = []       # index of seat num (0 ~ N-1), in order

    # brutal force
    def seat(self) -> int:
        if not self.sit:
            self.sit.append(0)
            return 0
        if len(self.sit) == self.seat_num:
            return None
        gap = 0
        if 0 in self.sit:
            pre = 0
        else:
            pre = -1
        to_sit = None
        to_insert = None
        for i in range(len(self.sit)):
            g = (pre + self.sit[i])//2 - pre
            if g > gap:
                gap = g
                to_sit = pre + g
                to_insert = i
            pre = self.sit[i]
        if self.sit[-1] != self.seat_num - 1:
            g2 = (self.seat_num + self.sit[-1])//2 - self.sit[-1]
            if g2 > gap:
                to_sit = self.seat_num - 1
                to_insert = len(self.sit)

        self.sit.insert(to_insert, to_sit)
        return to_sit       

    def leave(self, p: int) -> None:
        if p in self.sit:
            self.sit.remove(p)
        



def test():
    # er = ExamRoom(10)
    # print(er.seat())    # 0
    # print(er.seat())    # 9
    # print(er.seat())    # 4
    # print(er.seat())    # 2
    # print(er.leave(4))    # 
    # print(er.seat())    # 5

    print('-'*10)
    er = ExamRoom(4)
    print(er.seat())    # 0
    print(er.seat())    # 3
    print(er.seat())    # 1
    print(er.seat())    # 2
    print(er.leave(1))    # 
    print(er.leave(3))    # 
    print(er.seat())    # 1




test()
