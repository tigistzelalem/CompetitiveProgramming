class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        right = 0
        for i in range(len(nums)):
            if nums[i] != 0 and nums[right] == 0:
                nums[i], nums[right] = nums[right], nums[i]
            if nums[right] != 0:
                right += 1
