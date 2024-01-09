class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        while left < len(nums):
            if nums[left] == val:
                nums.pop(left)
                left -= 1
            left += 1

        return len(nums)