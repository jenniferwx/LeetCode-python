class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        row = len(matrix)
        col = len(matrix[0])
        if row<1 or col<1:
            return False
        
        i = 0
        j = col-1
        while(i<row and j>=0):
            if matrix[i][j]==target:
                return True
            elif matrix[i][j]<target:
                i +=1
            else:
                j -=1
        
        return False
