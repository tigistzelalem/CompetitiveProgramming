class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        ans = 0
        
        for i in range(len(nums)):
            if nums[i] - diff in nums and nums[i] - 2 * diff in nums:
                ans += 1
                
        return ans