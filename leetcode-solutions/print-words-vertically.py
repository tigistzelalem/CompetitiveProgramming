class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        max_len = max(len(word) for word  in words)
        max_cols = max_len
        cols = []
        for i in range(max_cols):
            col = ''
            for word in words:
                if i < len(word):
                    col += word[i]
                else:
                    col += ' '
            cols.append(col.rstrip())
        return cols
