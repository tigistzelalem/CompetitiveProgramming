class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        seen = set()
        ans = 0
        for r in rolls:
            seen.add(r)
            if len(seen) == k:
                ans += 1
                seen.clear()
        
        return ans + 1