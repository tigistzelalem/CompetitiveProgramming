class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:

        left = 0
        count = 0
        pre_sum = 0

        while  pre_sum < n:
            if left <len(nums) and nums[left] <= pre_sum + 1:
                pre_sum += nums[left]
                left += 1
            
            else:
                count += 1
                pre_sum += (pre_sum + 1)
            
        return count

            



