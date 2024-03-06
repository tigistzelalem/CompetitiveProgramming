class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        ans = [float('inf'), -1]

        if target not in nums:
            return [-1, -1]
       
        
        for i in range(len(nums)):
            if nums[i] == target:
                ans= [min(ans[0], i), max(ans[1], i)]
        
        return ans
        