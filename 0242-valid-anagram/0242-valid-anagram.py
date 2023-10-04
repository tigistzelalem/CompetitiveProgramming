class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        
        if n != m:
            return False
        
        s = sorted(s)
        t = sorted(t)
        
        if s != t :
            return False
        
        return True
    