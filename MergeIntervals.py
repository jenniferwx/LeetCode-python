# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
#    def compare(Interval):
#        return Interval.start
    def merge(self, intervals):
        res = []
        if(len(intervals)<=0):
            return res
        intervals.sort(key = lambda x: x.start)    
        #sorted(intervals, key=lambda [start,end]: start)
        LastInterval = intervals[0]
        for interval in intervals[1:]:
            if LastInterval.end >= interval.start:
                LastInterval.end = max(LastInterval.end, interval.end)
            else:
                res.append(LastInterval)
                LastInterval = interval
        
        res.append(LastInterval) 
        return res       
            
