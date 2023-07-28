class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        count = 0
        max_arr = 0 
        start = 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            while count > 1:
                if nums[start] == 0:
                    count -= 1
                start += 1
                
            max_arr = max(max_arr, i - start)
        return max_arr
        
        
        
        
        
        
        