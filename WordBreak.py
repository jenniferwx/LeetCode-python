'''
Given a string s and a dictionary of words dict, determine if s can be segmented into a
space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code". 
'''
class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        L = len(s)
        res = [False]*(L+1)
        res[0] = True
        
        for i in range(1,L+1):
            for j in range(i-1,-1,-1):
                ch = s[j:i]
                if ch in dict and res[j]:
                    res[i] = True
                    break
        
        return res[L]  
