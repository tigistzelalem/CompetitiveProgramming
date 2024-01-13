class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        counts = {}
        left = 0
        right = 0
        total = 0
        ans = 0

        while right < len(nums):
            counts[nums[right]] = counts.get(nums[right], 0) + 1
            total += nums[right]
            right += 1

            while len(counts) != right - left:
                counts[nums[left]] -= 1
                if counts[nums[left]] == 0:
                    del counts[nums[left]]
                total -= nums[left]
                left += 1

            ans = max(ans, total)
        return ans









        

