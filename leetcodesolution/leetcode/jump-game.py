class Solution:
    def canJump(self, nums: List[int]) -> bool:
        gaps = 0
        for num in nums:
            if gaps < 0:
                return False
            elif num > gaps:
                gaps = num
            gaps -= 1

        return True