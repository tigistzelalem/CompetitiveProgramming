class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        min_len = float('inf')
        last = {}
        for i, num in enumerate(cards):
            if num in last:
                length = i - last[num] + 1
                min_len=min(min_len, length)
            last[num] = i
        if min_len == float('inf'):
            return -1

        return min_len
