class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_recolor = float('inf')
        for i in range(len(blocks) - k +1):
            window = blocks[i: i+k]

            count = 0
            for char in window:
                if char == "W":
                    count += 1

            min_recolor = min(min_recolor, count)
            
        return min_recolor