class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n = len(nums)
        zeros = [0] * n
        ones = [0] * n 

        for i in range(n):
            if nums[i] == 0:
                zeros[i] += zeros[i-1] + 1
            else:
                zeros[i] = zeros[i-1]
        zeros.insert(0,0)
        nums = nums[::-1]
        for j in range(len(nums)):
            if nums[j] == 1:
                ones[j] += ones[j-1] + 1
            else:
                ones[j] = ones[j-1]
        ones.reverse()
        ones.append(0)
        
        maxi = float('-inf')
        result = []
        for i in range(len(zeros)):
            curr_sum = zeros[i] + ones[i]
            if curr_sum > maxi:
                maxi = curr_sum
                result = [i]
            elif curr_sum == maxi:
                result.append(i)
        return result




        


        