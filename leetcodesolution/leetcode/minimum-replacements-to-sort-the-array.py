class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:

        n = len(nums)
        minMaxVal = nums[n - 1]  
        ans = 0 

        for i in range(n - 2, -1, -1):
            if nums[i] > minMaxVal:  
                parts = nums[i] // minMaxVal  
                if nums[i] % minMaxVal:
                    parts += 1 
                minMaxVal = nums[i] // parts  
                ans += parts - 1  
            else:
                minMaxVal = nums[i]  
        return ans 