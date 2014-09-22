class Solution:
    # @return an integer
    def romanToInt(self, s):
        roman = {}
        roman['M'] = 1000;
        roman['D'] = 500;
        roman['C'] = 100;
        roman['L'] = 50;
        roman['X'] = 10;
        roman['V'] = 5;
        roman['I'] = 1;
        
        sum = 0
        L = len(s)
        if not s:
            return sum
            
        for i in range(L):
            if i<L-1 and roman[s[i]]< roman[s[i+1]]:
                sum -= roman[s[i]]
            else:
                sum += roman[s[i]]
            
            
        return sum    
