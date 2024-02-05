class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        count = 0
        max_len = 0
        start = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            while count > 1:
                if nums[start] == 0:
                    count -= 1
                start += 1

            max_len = max(max_len, i - start)

        return max_len



        
       