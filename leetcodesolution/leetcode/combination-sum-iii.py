class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        currSum = 0

        def backtrack(idx, path, currSum):

            if len(path) == k and currSum == n:
                ans.append(path.copy())
                return
            
            if idx > 9 or currSum > n:
                return

            # take
            path.append(idx)
            backtrack(idx + 1, path, currSum + idx)
            path.pop()

            # leave
            backtrack(idx + 1, path, currSum)
        
        backtrack(1, [], 0)
        return ans
