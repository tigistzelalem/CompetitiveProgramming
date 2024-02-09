class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:

        pre = [0]*(len(nums) + 1)
        pre_sum = [0]*(len(nums) + 1)

        for left, right in requests:
            pre[left] += 1
            pre[right + 1] -= 1
        
        for i in range(len(pre)):
            pre_sum[i] += pre_sum[i-1] + pre[i] 

        nums = sorted(nums, reverse=True)
        pre_nums = sorted(pre_sum, reverse=True)

        ans = []
        for i in range(len(nums)):
            ans.append(nums[i]*pre_nums[i])

        return sum(ans) %(10**9 + 7)




