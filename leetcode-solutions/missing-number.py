class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # n = len(nums)
        # total = n * (n+1) // 2
        
        # for num in nums:
        #     total -= num
        # return total
        nums.sort()
        for i , num in enumerate(nums):
            if i != num:
                return i
   
        return i + 1

            
        
