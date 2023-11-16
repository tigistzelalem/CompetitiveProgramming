class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        
        left = 0
        sets = set()
        for right in range(len(nums) // 2, len(nums)):
            if nums[right] > nums[left] and left not in sets:
                sets.add(left)
                sets.add(right)
                left += 1
        
        return len(nums) - len(sets)