class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        counts = {}
        for i, val in enumerate(nums):
            counts[val] = counts.get(val, 0) + 1
            
        freq = len(nums) / 2
        result = None
        
        for num, count in counts.items():
            if count > freq:
                result = num
                break   
        return num
            
            
            