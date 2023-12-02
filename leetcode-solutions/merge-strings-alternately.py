class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m = len(word1)
        n = len(word2)
        left = right = 0
        result = []

        while left < m or right < n:
            if left < m:
                result += word1[left]
                left += 1
            if right < n:
                result += word2[right]
                right += 1
        return ''.join(result)
