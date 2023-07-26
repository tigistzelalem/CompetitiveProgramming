class Solution:
    def isGood(self, nums: List[int]) -> bool:
        base = len(nums) - 1
        res = defaultdict(int)
        
        for i in nums:
            if i > base:
                return False
            res[i] += 1
            
            if (i != base and res[i] > 1):
                return False
            if res[base] > 2:
                return False
        return True
        