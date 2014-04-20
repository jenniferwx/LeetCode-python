class Solution:
    # @param A a list of integers
    # @param target an integer
    # @return a boolean
    def search(self, A, target):
        left = 0
        right = len(A)-1
        while(left<=right):
            mid = (left+right)/2
            if(target == A[mid]):
                return True
            else:    
                if(A[left]<A[mid]):
                    if (target>=A[left] and target<=A[mid]):
                        right = mid-1
                    else:
                        left = mid+1
                elif(A[mid]<A[right]):
                    if (target>=A[mid] and target<=A[right]):
                        left = mid+1
                    else:
                        right = mid-1
                elif(A[left]==A[mid]):
                    left = left +1
                elif(A[mid]==A[right]):
                    right = right-1
                    
        return False        
           
