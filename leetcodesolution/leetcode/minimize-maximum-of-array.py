class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans = 0
        _sum = 0
        for i in  range(len(nums)):
            _sum += nums[i]
            avg = _sum / (i+1)

            if avg > ans:
                ans = avg
        
        return ceil(ans)
        