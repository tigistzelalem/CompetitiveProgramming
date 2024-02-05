class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')
        left = 0
        right = 0
        ans = 0

        while right < len(nums):
            ans += nums[right]
            right += 1

            while left < right and ans >= target:
                ans -= nums[left]
                left += 1
                min_len = min(min_len, right - left + 1)
        
        if min_len == float('inf'):
            return 0
        
        return min_len

        