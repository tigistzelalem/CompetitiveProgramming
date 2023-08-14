class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        
        Sum, ans = 0, 0
        
        for val in nums:
            Sum += val
            ans = min(ans, Sum)
        return -ans + 1