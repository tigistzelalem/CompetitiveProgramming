class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count = {}
        
        for char in t:
            count[char] = count.get(char, 0) +1
        
        for char in s:
            count[char] -= 1
            if count[char] == 0:
                del count[char]
                
        return list(count.keys())[0]
                
            