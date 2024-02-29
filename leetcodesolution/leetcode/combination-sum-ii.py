class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        currSum = 0
        candidates.sort()
        def backtrack(idx, currSum, path):

            if currSum == target:
                ans.append(path[:])
                return
            
            for i in range(idx, len(candidates)):
                
                if candidates[i] == candidates[i-1] and i > idx:
                    continue

                if currSum + candidates[i] > target:
                    break

                # take
                path.append(candidates[i])
                backtrack(i + 1, currSum + candidates[i], path)
                path.pop()


        backtrack(0, 0, [])
        return ans

