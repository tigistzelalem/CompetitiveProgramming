class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans = 0
        count = 0
        pre_sum = [0]*k
        pre_sum[0] = 1

        for num in nums:
            count = (count + num % k + k) % k
            ans += pre_sum[count]

            pre_sum[count] += 1
        
        return ans


