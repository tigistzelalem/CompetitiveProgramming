class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        ans = []
        nums.sort()
        l = 0
        r = len(nums) - 1
        avg = 0
        while l < r:
            ans.append((nums[l] + nums[r]) / 2)
            l += 1
            r -= 1
        return len(set(ans))