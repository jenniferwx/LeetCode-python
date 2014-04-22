class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        length = 0
        for i in range(len(s)-1,-1,-1):
            if(s[i].isalpha()):
                length +=1
            elif length!=0 and not s[i].isalpha():
                break
            
        return length  
