class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = {}
        n = len(nums)
        result = set()
        
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            
            if counts[num] > n / 3:
                result.add(num)
                
        return list(result)