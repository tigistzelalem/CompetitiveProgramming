class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        lis = []
        for i in range(len(nums)):
             lis.append(nums[i] + nums[len(nums)-1-i])
        return max(lis)