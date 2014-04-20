class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        res = []
        inserted  = False
        for interval in intervals:
            if inserted or interval.end < newInterval.start:
                res.append(Interval(interval.start,interval.end))
            elif newInterval.end < interval.start:
                res.append(newInterval)
                res.append(interval)
                inserted = True
            else:
                newInterval.start = min(newInterval.start, interval.start)
                newInterval.end = max(newInterval.end,interval.end)
        if(not inserted):
            res.append(newInterval)
        
        return res    
