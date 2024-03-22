class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        ans = []
        for key, val in counts.items():
            if val == 2:
                ans.append(key)
        
        return ans
            