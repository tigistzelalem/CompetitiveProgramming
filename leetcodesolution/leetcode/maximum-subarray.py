class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_ = nums[0]
        total = 0

        for num in nums:
            if total < 0:
                total = 0
            total += num
            max_ = max(max_ ,total)
        
        return max_
        