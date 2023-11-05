class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        
        pointer1 = 2
        slow = pointer1
        
        for fast in range(pointer1, len(nums)):
            if nums[fast] != nums[slow- pointer1]:
                nums[slow] = nums[fast]
                slow += 1
        
        return slow
            
                
            