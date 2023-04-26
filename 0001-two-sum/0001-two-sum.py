class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in res:
                return [ res[diff],i]
            res[n] = i
        return
