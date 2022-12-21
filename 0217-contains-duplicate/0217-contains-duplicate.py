class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        list = set(nums)
        if len(list) != len(nums):
            return True
        else:
            return False
        