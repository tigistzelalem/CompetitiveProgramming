class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        left = 0
        right = len(nums) - 1
        sorted_nums = sorted(nums)
        
        while left < len(nums):
            if nums[left] != sorted_nums[left]:
                break
            left += 1
        while right > left:
            if nums[right] != sorted_nums[right]:
                break
            right -= 1
        return right - left +1