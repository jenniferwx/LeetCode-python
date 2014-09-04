class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def findMax(self, array):
        if not array:
            return 0
        L = len(array)
        Max = -1
        for i in range(L):
            left = i
            while(left-1>=0 and array[left-1]>=array[i]):
                left -=1
            right =i
            while(right+1<L and array[right+1]>=array[i]):
                right +=1
            res = (right-left+1)*array[i]
            if res>Max:
                Max = res
        return Max
        
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        L = [0]*n
        Max = -1
        for i in range(m):
            for j in range(n):
                if(matrix[i][j]=='1'):
                    L[j] += 1
                else:
                    L[j] = 0
                    
            res = self.findMax(L)
            if(res>Max):
                Max = res
        return Max
