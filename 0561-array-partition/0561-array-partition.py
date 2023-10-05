class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        res = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                res += nums[i]
        
        return res
            