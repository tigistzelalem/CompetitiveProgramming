class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        
        if k == 1:
            return 0

        pre_sum = [0]*(len(weights) - 1)

        for i in range(len(weights) - 1):
            pre_sum[i] = weights[i] + weights[i+1]
        
        pre_sum.sort() 
        return sum(pre_sum[-k+1:]) - sum(pre_sum[:k - 1])

        


