class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float('inf')
        start = 0
        end = 0
        res = 0
        
        while end < len(nums):
            res += nums[end]
            end += 1
            
            while start < end and res >= target:
                res -= nums[start]
                start += 1
                
                min_length = min(min_length, end - start + 1)
        if min_length == float('inf'):
            return 0
                
        return min_length
        