class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        nums = []
        if numNegOnes:
            nums += [-1]*numNegOnes
        if numZeros:
            nums += [0]*numZeros
        if numOnes:
            nums +=[1]*numOnes
        n = len(nums)
        return sum(nums[n - k:])
       
        
        