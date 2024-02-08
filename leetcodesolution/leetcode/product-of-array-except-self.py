class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_sum = [1]*len(nums)
        suff_sum = [1]*len(nums)
        ans = []

        for i in range(1, len(nums)):
            pre_sum[i] = pre_sum[i-1] *nums[i-1]
        
        for i in range(1, len(nums)):
            suff_sum[i] = suff_sum[i-1] * nums[-i]
        
        for i in range(len(nums)):
            ans.append(suff_sum[-i-1] * pre_sum[i])
        
        return ans

        