class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = 0
        nums = sorted(nums)
        
        if len(nums) == 1:
            return False
        
        
        for i in range(len(nums)):
            if nums[i] == nums[i-1]:
                count += 1
            
            if count == 1:
                return True
        return False
        
        
        