class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        L = len(A)
        left = [0]*L
        right = [0]*L
        leftmost = 0
        rightmost = 0
        for i in range(L):
            if A[i]> leftmost:
                leftmost = A[i]
                left[i] = A[i]
            else:
                left[i] = leftmost
        
        for i in range(L-1,-1,-1):
            if A[i]>rightmost:
                rightmost = A[i]
                right[i] = A[i]
            else:
                right[i] = rightmost
        
        res = 0
        for i in range(L):
            res += min(left[i],right[i])-A[i]
        
        return res    
