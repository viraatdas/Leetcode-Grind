class Solution:
    def solve(self, n):
        # Write your code here
        def condition(num):
            l = [3,6,9]
            if num%3==0:
                return True
            while num:
                if num%10 in l:
                    return True
                num//=10
            return False
        
        return ["clap" if condition(i) else str(i) for i in range(1,n+1)]
