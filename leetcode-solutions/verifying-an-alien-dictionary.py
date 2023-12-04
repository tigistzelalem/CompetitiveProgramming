class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        char_map = {}
        for i, char in enumerate(order):
            char_map[char] = i
        for i in range(1, len(words)):  # Start from index 1
            word1 = words[i-1]
            word2 = words[i]
            for j in range(min(len(word1), len(word2))):
                char1 = word1[j]
                char2 = word2[j]
                if char_map[char1] < char_map[char2]:
                    break
                elif char_map[char1] > char_map[char2]:
                    return False
            else:
                if len(word1) > len(word2):
                    return False
        return True