class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count = 0
        left = 0
        right = left + 1
        while left < len(nums) - 1:

            while right < len(nums):
                if nums[left] == nums[right] and (left*right) % k == 0:
                    count += 1
                right += 1
            left += 1
            right = left + 1

        return count