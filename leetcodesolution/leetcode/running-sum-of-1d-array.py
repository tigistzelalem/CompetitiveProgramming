class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        pre_sum = [0] * len(nums)
        pre_sum[0] = nums[0]
        for i in range(1, len(nums)):
            pre_sum[i] += nums[i]+ pre_sum[i-1]
        
        return pre_sum