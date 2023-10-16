class Solution:
    def reverseVowels(self, s: str) -> str:
        vowls = "aeiouAEIOU"
        l = 0
        r = len(s) - 1
        word = list(s)
        
        while l < r:
            while l < r and vowls.find(word[l]) == -1:
                l += 1
            while l < r and vowls.find(word[r]) == -1:
                r -= 1
            word[l], word[r] = word[r], word[l]
            l += 1
            r -= 1
        
        return ''.join(word)