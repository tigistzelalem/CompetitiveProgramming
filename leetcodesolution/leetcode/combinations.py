class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        path = []
        ans = []
        def backtrack(num):
            if len(path) == k:
                ans.append(path.copy())
                return
            for ele in range(num+1, n + 1):
                path.append(ele)
                backtrack(ele)
                path.pop()
        backtrack(0)

        return ans