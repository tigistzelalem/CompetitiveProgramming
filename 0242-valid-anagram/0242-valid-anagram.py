class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        t = sorted(t)
        s = sorted(s)
        for i in range(len(s)):
            if t[i] != s[i]:
                return False
        return True