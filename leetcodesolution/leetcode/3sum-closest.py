class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n <= 3:
            return sum(nums)
        
        nums = sorted(nums)
        minSum, minDiff = None, inf
        
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left, right = i + 1, n - 1
            
            while left < right: 
                currSum = sum([nums[i], nums[left], nums[right]])
                currDiff = abs(target - currSum)
                
                if currDiff < minDiff:
                    minDiff = currDiff
                    minSum = currSum
                    
                if minDiff == 0:
                    return minSum
                
                if target > currSum:
                    left+= 1
                   
                else:
                    right -= 1
                   
        return minSum
    