class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        ans = []
        total = sum(nums)
        pre_sum = 0

        for i, num in enumerate(nums):
            suf_sum = total - num - pre_sum
            left_size = i
            right_size = len(nums) - i -1

            ans.append(left_size*num - pre_sum + suf_sum - right_size*num)

            pre_sum += num

        return ans




        