class Solution:
    def solve(self, nums, k):
        # Write your code here
        seen = set()
        
        for i in nums:
            if k - i in seen:
                return True
            seen.add(i)
        return False
