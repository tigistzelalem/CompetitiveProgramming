class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()

        # Find the median
        n = len(nums)
        median = nums[n//2]

        # Initialize new array
        new_arr = [None] * n

        # Populate new array with numbers smaller than median on odd indices
        # and the rest on even indices
        i = 1
        j = 0
        for num in nums:
            if num < median:
                new_arr[i] = num
                i += 2
            else:
                new_arr[j] = num
                j += 2

        return new_arr


