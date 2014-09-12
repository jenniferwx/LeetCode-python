class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        num.sort()
        L = len(num)
        res = []
        if L<3:
            return res
        
        for i in range(0,L-2):
            begin = i+1
            end = L-1
            if num[i]>0:
                break
            if i>0 and num[i]==num[i-1]:
                continue
            while begin<end:
                subsum = num[i]+num[begin]+num[end]
                if subsum==0:
                    res.append([num[i],num[begin],num[end]])
                    begin+=1
                    end-=1
                    while(begin<end and num[begin]==num[begin-1]):
                        begin +=1
                    while(begin<end and num[end]== num[end+1]):
                        end -=1
                elif subsum>0:
                    end -=1
                else:
                    begin+=1
        
        return res        
        
