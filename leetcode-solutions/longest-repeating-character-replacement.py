class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_len = 0
        max_count = 0
        counts = {}

        for right in range(len(s)):
            counts[s[right]] = counts.get(s[right], 0) + 1
            max_count = max(max_count, counts[s[right]])

            if (right - left + 1) - max_count > k:
                counts[s[left]] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)

        return max_len

        

        