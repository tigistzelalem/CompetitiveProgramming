class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        transpose = [[0 for _ in range(m)] for _ in range(n)]

        for j in range(n):
            for i in range(m):
                transpose[j][i] = matrix[i][j]

        return transpose