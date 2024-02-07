class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix =  matrix
        rows, cols = len(matrix), len(matrix[0])
        self.pre_sum = [[0 for i in range(cols + 1)] for j in range(rows + 1)]
        if cols > 0 and rows > 0:
            for row in range(1, rows + 1):
                for col in range(1, cols + 1):
                    self.pre_sum[row][col] = self.pre_sum[row-1][col] + self.pre_sum[row][col-1] - self.pre_sum[row - 1][col-1] + self.matrix[row-1][col-1]
        else:
            self.pre_sum = [[0]]
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:


        rows, cols = len(self.matrix), len(self.matrix[0])
        
        row1 = max(0, min(row1, rows - 1))
        row2 = max(0, min(row2, rows - 1))
        col1 = max(0, min(col1, cols - 1))
        col2 = max(0, min(col2, cols - 1))
        
        sub_sum = (
            self.pre_sum[row2 + 1][col2 + 1]
            - self.pre_sum[row2 + 1][col1]
            - self.pre_sum[row1][col2 + 1]
            + self.pre_sum[row1][col1]
        )

        return sub_sum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)