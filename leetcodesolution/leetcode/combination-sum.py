class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def backtrack(idx, path, curr_sum):
            if curr_sum == target and path not in ans:
                ans.append(path.copy())
                return

            if idx >= len(candidates) or curr_sum > target:
                return
            
            # take and next
            path.append(candidates[idx])
            backtrack(idx + 1, path, curr_sum + candidates[idx])
            path.pop()
            
            # take and repeat
            path.append(candidates[idx])
            backtrack(idx, path, curr_sum + candidates[idx])
            path.pop()

            # leave
            backtrack(idx + 1, path, curr_sum)

        backtrack(0,[], 0)
        return ans
            

            
