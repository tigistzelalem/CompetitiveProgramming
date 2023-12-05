class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first = set('qwertyuiop')
        second = set('asdfghjkl')
        third = set('zxcvbnm')

        ans = []
        for word in words:
            word_lower = word.lower()
            if all(char in first for char in word_lower) or \
                all(char in second for char in word_lower) or \
                all(char in third for char in word_lower):
                ans.append(word)

        return ans