class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        counts = {}
        for _, val in enumerate(nums):
            counts[val] = counts.get(val, 0) + 1
        threshold = len(nums) / 2
        result = None
        for num, count in counts.items():
            if count > threshold:
                result = num
                break   
        return num
            
            
            