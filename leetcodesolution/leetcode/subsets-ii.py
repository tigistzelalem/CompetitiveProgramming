class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        def backtrack(idx, path):
           
            if path not in ans:
                ans.append(path.copy())

            if idx >= len(nums):
                return

            path.append(nums[idx])
            backtrack(idx + 1, path)
            path.pop()

            backtrack(idx + 1, path)
        
        backtrack(0, [])
        return ans
            