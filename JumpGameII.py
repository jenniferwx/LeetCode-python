'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to
the last index.)
'''

class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        L = len(A)
        start = 0
        end = 0
        step = 0
        if(L<=0):
            return 0
        while(start < L-1):
            end = start + A[start]
            step = step + 1
            if(end >= L-1):
                return step
            nextstart = start    
            for i in range(start+1,end+1):
                if (i+A[i]) >= (nextstart+A[nextstart]):
                    nextstart = i
            start = nextstart
        
        return step  
