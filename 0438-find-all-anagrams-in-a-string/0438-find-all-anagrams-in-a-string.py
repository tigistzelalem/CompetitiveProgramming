class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        
        left, right = 0, 0
        res = []
        count = Counter(p)
        
        for i, c in enumerate(s):
            count[c] -= 1
            left += 1
            
            while count[c] < 0:
                count[s[right]] += 1
                right += 1
                left -= 1
            if left == len(p):
                res.append(right)
        return res