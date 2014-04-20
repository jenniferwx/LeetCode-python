class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        New = []
        for ch in s:
            if (ch>='0' and ch<='9') or (ch>='a' and ch<='z'):
                New.append(ch)
            elif ch>='A' and ch<='Z':
                New.append(chr(ord(ch) - ord('A') + ord('a')))
        
        return New == New[::-1]        
