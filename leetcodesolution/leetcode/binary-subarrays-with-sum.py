class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
   
        res = 0
        curSum = 0
        preSum = { 0:1 }
        
        for n in nums:
            curSum += n
            diff = curSum - goal

            res += preSum.get(diff, 0)
            preSum[curSum] = 1 + preSum.get(curSum, 0)
            
        return res

        