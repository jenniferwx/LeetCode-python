class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        L1 = len(a)
        L2 = len(b)
        res = ""
        carry = 0
        i = L1-1
        j = L2-1
        while(i>=0 or j>=0):
            num = carry
            if i>=0:
                num = num + int(a[i])
                i = i-1
            if j>=0:    
                num = num + int(b[j])
                j = j-1
            res = str(num%2) + res 
            carry = num/2
        if(carry==1):
            res = str(carry) + res 
        return res    
        
