class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        ans = {}
        
        for i in range(len(nums)):
            if nums[i] in ans and i - ans[nums[i]] <= k:
                return True
            ans[nums[i]] = i
        return False