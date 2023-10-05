class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        dupl = -1
        missing = 1
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                dupl = nums[i]
            elif nums[i] > nums[i-1] + 1:
                missing = nums[i-1] + 1
        return [dupl, len(nums) if nums[-1] != len(nums) else missing]
        