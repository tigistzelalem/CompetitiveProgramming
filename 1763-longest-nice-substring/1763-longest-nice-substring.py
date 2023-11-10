class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        
        max_len = 0
        result = ""

        for i in range(len(s)):
            for j in range(i + max_len, len(s)):
                substring = s[i:j + 1]
                if all(c.swapcase() in substring for c in substring) and j - i + 1 > max_len:
                    max_len = j - i + 1
                    result = substring

        return result

            
            