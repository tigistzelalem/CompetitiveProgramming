class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total = sum(cardPoints)
        window_size = n - k
        window_sum = sum(cardPoints[:window_size])
        min_sum = window_sum
        
        for i in range(window_size, n):
            window_sum += cardPoints[i] - cardPoints[i - window_size]
            min_sum = min(min_sum, window_sum)
        ans = total - min_sum 
        return ans
       