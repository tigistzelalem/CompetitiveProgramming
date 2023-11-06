class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        slow = 0
        fast = slow + 1
        
        while fast < len(nums):
            if nums[slow] == nums[fast]:
                return nums[slow]
            slow += 1
            fast += 1
            