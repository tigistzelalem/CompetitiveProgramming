class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        min_len = float('inf')
        for char in range(len(blocks) - k + 1):
            sub_block = blocks[char: char+k]
            
            count = 0
            for char in sub_block:
                if char == 'W':
                    count += 1
            min_len = min(min_len, count)
                
        return min_len