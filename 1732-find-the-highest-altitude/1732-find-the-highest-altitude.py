class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        n = len(gain)
        prefix_sum = []
        prefix_sum.append([0][0])
        
        
        for i in range(n):
            prefix_sum.append(prefix_sum[-1] + gain[i])
        return max(prefix_sum)
       
