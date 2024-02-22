class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        ans = [1]
        if rowIndex == 0:
            return [1]
        
        result = self.getRow(rowIndex - 1)
        for i in range(len(result) - 1):
            ans.append(result[i] + result[i+1])

        ans.append(1)

        return ans

        