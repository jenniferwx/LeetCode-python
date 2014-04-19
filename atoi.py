'''
Implement atoi to convert a string to an integer.
'''

class Solution:
    # @return an integer
    def atoi(self, str):
        res = 0
        L0 = len(str)
        if(L0<=0):
            return res
        i = 0
        while(str and str[0]==' '):
            str = str[1:]
        
        negative = False
        if(str[i]=='-'):
            negative = True
            str = str[i+1:]
        if(str[i]=='+'):
            str = str[i+1:]
        L = len(str)
        
        for i in range(L):
            if str[i]>='0' and str[i]<='9':
                res = res*10 + int(str[i])
            else:
                break
        
        if negative:
            res = res*(-1)

        if(res>2147483647):
            res = 2147483647
        if(res<-2147483648):
            res = -2147483648
        
        return res    
           
