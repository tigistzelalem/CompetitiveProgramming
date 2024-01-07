class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        counts = {'T': 0, "F": 0}
        max_ = 0
        left = 0

        for right in range(n):
            counts[answerKey[right]] += 1
            max_ = max(counts.values())
            if max_ + k < right - left + 1:
                 counts[answerKey[left]] -= 1
                 left += 1
            max_ = max(max_, right - left + 1)

        return max_
        