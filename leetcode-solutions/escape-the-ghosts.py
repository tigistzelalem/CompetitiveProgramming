class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:

        x, y = target
        start_dist = abs(x)  + abs(y)
        for x2, y2 in ghosts:
            _dist = abs(x - x2) + abs(y - y2)
            if _dist <= start_dist:
                return False

        return True
           
