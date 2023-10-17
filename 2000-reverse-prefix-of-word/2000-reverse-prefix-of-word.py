class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        ans = list(word)
        left = 0
        
        for i in range(len(word)):
            if ans[i] == ch:
                while left <= i:
                    ans[i], ans[left] = ans[left], ans[i]
                    left += 1
                    i -= 1
                return ''.join(ans)
        return word