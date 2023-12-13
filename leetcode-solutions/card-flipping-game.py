class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:

        min_good = float('inf')
        sets = set()

        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                sets.add(fronts[i])
        
        for i in (fronts + backs):
            if i not in sets:
                min_good = min(min_good, i)
        
        return min_good if min_good != float('inf') else 0






