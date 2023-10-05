class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        n = len(nums)
    
        if n < 2:
            return -1

        max_val = float('-inf')
        maxIndex = -1

        for i in range(n):
            if nums[i] > max_val:
                max_val = nums[i]
                maxIndex = i
            elif nums[i] == max_val:
                maxIndex = -1 

        if maxIndex == -1:
            return -1 

        for i in range(n):
            if i != maxIndex and max_val < 2 * nums[i]:
                return -1

        return maxIndex