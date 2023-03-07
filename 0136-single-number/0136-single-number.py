class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = Counter(nums)
        items = count.items()
        for key, val in items:
            if val == 1:
                ans = key
                break
        return ans
    
