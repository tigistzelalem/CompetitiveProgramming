class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # for i in range(k):
        #     prev = nums[-1]
        #     for j in range(len(nums)):
        #         nums[j], prev = prev, nums[j]
        
        if k == 0:
            return nums
        
        k = k % len(nums)
        length = len(nums)
        
        nums[length - k:], nums[:length - k] = nums[:length - k], nums[length - k:]
        