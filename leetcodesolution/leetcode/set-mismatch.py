class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dupl = -1
        missing = -1
        for i in range(1, len(nums) + 1):
            count = nums.count(i)
            if count == 2:
                dupl = i
            elif count == 0:
                missing = i
        
        return [dupl, missing]