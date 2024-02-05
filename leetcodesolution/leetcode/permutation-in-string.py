class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        left, right = 0, 0
        res = ""
        count = Counter(s1)
        
        for i, c in enumerate(s2):
            count[c] -= 1
            left += 1
            
            while count[c] < 0:
                count[s2[right]] += 1
                right += 1
                left -= 1
            if left == len(s1):
                res += s2[right]
        return res