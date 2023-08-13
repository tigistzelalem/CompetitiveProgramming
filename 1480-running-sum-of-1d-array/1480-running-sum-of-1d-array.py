class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        self.prefix = []
        self.prefix.append(nums[0])
        
        for i in range(1, len(nums)):
            self.prefix.append(self.prefix[-1] + nums[i])
        return self.prefix