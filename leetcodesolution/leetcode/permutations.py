class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(path):
            if len(path) == len(nums):
                ans.append(path.copy())
            
            for ele in nums:
                if ele not in path:
                    path.append(ele)
                    backtrack(path)
                    path.pop()
        backtrack([])

        return ans
