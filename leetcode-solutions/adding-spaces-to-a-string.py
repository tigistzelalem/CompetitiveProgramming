class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = ''
        pointer = 0
        for i, char in enumerate(s):
          if pointer < len(spaces) and i == spaces[pointer]:
            ans += ' '
            pointer += 1
          ans += char
        
        return ans
