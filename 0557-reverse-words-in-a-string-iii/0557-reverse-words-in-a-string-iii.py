class Solution:
    def reverseWords(self, s: str) -> str:
        
        res = []
        space_idx = -1
        
        for i in range(len(s)):
            if s[i] == ' ' or i == len(s) - 1:
                reverse_idx = i -1 if i != len(s) - 1 else i
                
                while reverse_idx > space_idx:
                    res.append(s[reverse_idx])
                    reverse_idx -= 1
                if i != len(s)-1:
                    res.append(' ')
                space_idx = i
                    
        return ''.join(res)