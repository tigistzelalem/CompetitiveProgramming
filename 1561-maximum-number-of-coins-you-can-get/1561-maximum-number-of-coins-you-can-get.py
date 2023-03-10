class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        val = 0
        for i in range(len(piles)//3, len(piles),2):
            val += piles[i]
        return val
            
            
       
