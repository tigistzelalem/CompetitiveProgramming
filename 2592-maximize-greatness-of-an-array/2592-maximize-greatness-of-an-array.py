class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort()
        left = 0
        
        for num in nums:
            if nums[left] < num:
                left += 1
                
        return left
        
                