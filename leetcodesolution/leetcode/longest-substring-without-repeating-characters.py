class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        max_len = 0
        start = 0

        for i, c in enumerate(s):
            while c in seen:
                seen.remove(s[start])
                start += 1
            seen.add(c)
            max_len = max(max_len, i - start + 1)
        
        return max_len