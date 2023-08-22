class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        min_changes = float('inf')
        
        for i in range(len(blocks) -k + 1):
            substr = blocks[i: i+k]
            changes = 0
            
            for char in substr:
                if char == 'W':
                    changes += 1
            min_changes = min(min_changes, changes)
        return min_changes