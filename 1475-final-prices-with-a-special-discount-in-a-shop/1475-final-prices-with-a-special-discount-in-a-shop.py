class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        stack = []
        
        for i in range(n):
            for j in range(1, n):
                if j > i and prices[j] <= prices[i]:
                    stack.append(prices[i] - prices[j])
                    break
            else:
                stack.append(prices[i])
        
        return stack
    
 
