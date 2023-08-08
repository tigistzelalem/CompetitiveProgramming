class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        map1 = []
        map2 = []
        
        if len(s) != len(t):
            return False
        for val in s:
            map1.append(s.index(val))
        for val in t:
            map2.append(t.index(val))
        if map1 == map2:
            return True
        return False