class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [0]*len(nums)
        i = 0
        p1 = len(nums) - 1
        p2 = len(nums) - 1
        
        while p2 >= 0:
            if nums[i] *nums[i] <= nums[p1]*nums[p1]:
                result[p2] = nums[p1]*nums[p1]
                p2 -= 1
                p1 -= 1
            else:
                result[p2] = nums[i] * nums[i]
                i += 1
                p2 -= 1
                
        return result
                
            
            
            
        
                