class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        def inBound(row, col):
            return 0 <= row < n and 0 <= col < m
        row = col = 0
        ans = 0
        while inBound(row, col):
            ans += mat[row][col]
            row += 1
            col += 1
        row = n - 1
        col = 0
        while inBound(row, col):
            ans += mat[row][col]
            row -= 1
            col += 1
        if n % 2 !=0:
            ans -= mat[n//2][n//2]


        return ans




