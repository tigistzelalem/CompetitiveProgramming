class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        nums.sort()
        min_diff = float('inf')
        

        for end in range(k-1, n):
            start = end - (k-1)
            cur_diff = nums[end] - nums[start]
            min_diff = min(min_diff, cur_diff)
            
        return min_diff
            
            
        
            
            
        
        
        
        