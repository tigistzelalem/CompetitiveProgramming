class Solution:
    def maxScore(self, s: str) -> int:
        left = 1
        ans = []
        while 1:
            if left == len(s):
                break
            ans.append(s[:left].count('0') + s[left:].count('1'))
            left += 1
        
        return max(ans)