class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        for left in range(len(nums)):
            min_index = left
            for right in range(left + 1, len(nums)):
                if nums[right] < nums[min_index]:
                    min_index = right
            nums[left], nums[min_index] = nums[min_index], nums[left]

        