class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = Counter(nums)
        max_len = 0
        print(count)
        for key in count:
            if key + 1 in count:
                max_len = max(max_len, count[key] + count[key + 1])
        return max_len
            