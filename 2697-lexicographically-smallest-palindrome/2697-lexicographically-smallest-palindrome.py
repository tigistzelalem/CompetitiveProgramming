class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        
        left = 0
        right = len(s) - 1
        s = list(s)
        while left < right:
            if s[left] != s[right]:
                if s[left] > s[right]:
                    s[left] = s[right]
                else:
                    s[right] = s[left]
            left += 1
            right -= 1
        
        return ''.join(s)
        