class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        min_ = float('inf')
        max_ = float('inf')

        for num in nums:
            if num <= min_:
                min_ = num
            elif num <= max_:
                max_ = num
            else:
                return True

        return False
                
