class Solution:
    def removePalindromeSub(self, s: str) -> int:
        left = 0
        right = len(s) - 1
        
        if (len(s) == 1):
            return 1
        
        while left < right:
            if s[left] != s[right]:
                return 2
            
            else:
                left += 1
                right -= 1
        
        return 1