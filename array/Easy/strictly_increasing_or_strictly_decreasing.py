class Solution:
    def solve(self, nums):
        # Write your code here
        if not nums or len(nums) < 2:
            return True
            
        isIncrease = True
        if nums[0] == nums[1]:
            return False
        if nums[0] > nums[1]:
            isIncrease = False
        
        for i in range(1, len(nums)):
            if isIncrease:
                if nums[i-1] >= nums[i]:
                    return False
            else:
                if nums[i-1] <= nums[i]:
                    return False
        return True
