class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        ans = []
        
        while left < right:
            ans.append(str(nums[left]) + str(nums[right]))
            left += 1
            right -= 1
        
        if left == right:
            ans.append(str(nums[left]))
            
        return sum(int(num) for num in ans)
        
        