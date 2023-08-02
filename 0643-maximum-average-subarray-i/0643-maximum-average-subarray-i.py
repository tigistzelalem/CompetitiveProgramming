class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur_sum = sum(nums[:k])
        res = cur_sum / k
        
        for i in range(1, len(nums) - k + 1):
            cur_sum = cur_sum - nums[i-1]
            cur_sum = cur_sum + nums[i+k-1]
            
            res = max(res, cur_sum/k)
        return res