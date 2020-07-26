class Solution:
    def solve(self, s):
        # Write your code here
        final=""
        l = 0
        r = 1
        
        count = 0
    
    
        while r < len(s):
            if s[l] == s[r]:
                count+=1
            else:
                final+= str(count+1)+s[l]
                count = 0
            
            l = r
            r = l+1
            if r >= len(s):
                final+= str(count+1)+s[l]
        return final
        
