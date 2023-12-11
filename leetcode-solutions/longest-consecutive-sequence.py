class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        max_seq = 1
        count = 1
        if len(nums) <= 0:
            return 0
        for i in range(len(nums)):
            if nums[i] != nums[i-1]:
                if nums[i] == nums[i-1] + 1:
                    count += 1
                else:
                    count = 1
                max_seq = max(max_seq, count)

        return max_seq