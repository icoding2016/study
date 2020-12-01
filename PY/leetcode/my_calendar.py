# My Calendar II
# Implement a MyCalendarTwo class to store your events. 
# A new event can be added if adding the event will not cause a triple booking.
# Your class will have one method, book(int start, int end). 
# Formally, this represents a booking on the half open interval [start, end), the range of real numbers x such that start <= x < end.
# A triple booking happens when three events have some non-empty intersection (ie., there is some time that is common to all 3 events.)
# For each call to the method MyCalendar.book, return true if the event can be added to the calendar successfully without causing a triple booking.
#   Otherwise, return false and do not add the event to the calendar.
# Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)
#
# Example 1:
# MyCalendar();
# MyCalendar.book(10, 20); // returns true
# MyCalendar.book(50, 60); // returns true
# MyCalendar.book(10, 40); // returns true
# MyCalendar.book(5, 15); // returns false
# MyCalendar.book(5, 10); // returns true
# MyCalendar.book(25, 55); // returns true
# Explanation: 
# The first two events can be booked.  The third event can be double booked.
# The fourth event (5, 15) can't be booked, because it would result in a triple booking.
# The fifth event (5, 10) can be booked, as it does not use time 10 which is already double booked.
# The sixth event (25, 55) can be booked, as the time in [25, 40) will be double booked with the third event;
# the time [40, 50) will be single booked, and the time [50, 55) will be double booked with the second event.
 
# Note:
# The number of calls to MyCalendar.book per test case will be at most 1000.
# In calls to MyCalendar.book(start, end), start and end are integers in the range [0, 10^9].
#

# Solution 1: Counter. Every day has a counter   { date:count}
#   The solution is space consuming
#   T(max_end-min_start) 
#   
# Solution 2: count the open sessions
#    sort the event by starting time. 
#    go through these time point to count the active event(sessions). count + at start and close open sessions by end time.
#   E1          s1---e1
#   E2     s2-----e2
#   E3        s3---------e3
#   

# #  

from collections import defaultdict


# solution -- counter
# T(maxend-minstart)
# S(maxend-minstart)
class MyCalendar1(object):
    def __init__(self) -> None:
        self.events = []        # [(s,e),(s,e),...]
        self.calendar = defaultdict(int)

    def book(self, start:int, end:int)->bool:
        '''If new event wont cause tripple booking then book'''
        for i in range(start, end):
            if i in self.calendar and self.calendar[i] >= 2:
                return False
        for i in range(start, end):
            self.calendar[i] += 1
        self.events.append((start, end))
        #print(self.calendar)
        return True


# solution -- open sessions
# T(N*N)     -- N events, 
# S()
class MyCalendar2(object):
    def __init__(self) -> None:
        self.events = []        # [(s,e),(s,e),...],  events are sorted in ascending order

    def book(self, start:int, end:int)->bool:
        open_events = 0
        end_time = []
        events = sorted(self.events+[(start,end)], key=lambda x:x[0])
        for s,e in events:
            open_events += 1
            end_time.append(e)

            for ee in end_time:
                if ee <= s:
                    open_events -= 1
                    end_time.remove(ee)
            if open_events > 2:
                return False
        self.events = events
        return True
            


def test():
    mc = MyCalendar2()
    print(mc.book(10, 20)) # returns true
    print(mc.book(50, 60)) # returns true
    print(mc.book(10, 40)) # returns true
    print(mc.book(5, 15)) # returns false
    print(mc.book(5, 10)) # returns true
    print(mc.book(25, 55)) # returns true


test()

