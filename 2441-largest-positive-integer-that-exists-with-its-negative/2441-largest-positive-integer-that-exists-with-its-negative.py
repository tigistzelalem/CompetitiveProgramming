class Solution:
    def findMaxK(self, nums: List[int]) -> int:
#         ans = []
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] == -nums[j]:
#                     ans.append(abs(nums[i]))
                    
#         return max(ans) if ans else -1
            nums = sorted(nums, reverse=True)
            arr = set(nums)
            for i in range(len(nums)):
                if -nums[i] in arr:
                    return nums[i]
                
            return -1
       
                
              