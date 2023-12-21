class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m = len(strs)
        n = len(strs[0])
        count = 0

        for col in range(n):
            for row in range(1, m):
                if strs[row][col] < strs[row-1][col]:
                    count += 1
                    break

        return count
        