class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        p1 = 0
        
        for j in range(len(typed)):
            if p1 < len(name) and name[p1] == typed[j]:
                p1 +=1
            elif j == 0 or typed[j] != typed[j-1]:
                return False
        
        return p1 == len(name)