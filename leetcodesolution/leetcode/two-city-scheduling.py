class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff = []

        for a, b in costs:
            diff.append([a-b, [a,b]])
        diff.sort()
        sum_ = 0
        n = len(diff) // 2
        for i in range(len(diff)):
            if i < n:
                sum_ += diff[i][1][0]
            elif i >= n:
                sum_ += diff[i][1][1]
        
        return sum_ 

        