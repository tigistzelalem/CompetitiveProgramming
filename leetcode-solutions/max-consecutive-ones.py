class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current = 0
        max_ = 0
        start = -1

        for i in range(len(nums)):
            if nums[i] == 1:
                if start == -1 or nums[i-1] == 0:
                    start = i
                current += 1
            else:
                if current > max_:
                    max_ = current
                current = 0
        if current > max_:
            max_ = current
        return max_