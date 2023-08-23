class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        left_sum = [0] * n
        right_sum = [0] * n
        ans = []
        
        for i in range(1,n):
            left_sum[i] = left_sum[i-1] + nums[i-1]
        
        for i in range(1,n):
            right_sum[i] = right_sum[i-1] + nums[-i]
        
        for i in range(n):
            ans.append(abs(right_sum[-i-1] - left_sum[i]))
        
        return ans
            

        