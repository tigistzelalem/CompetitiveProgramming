class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        
        res = ''
        pointer = 0
        
        for i, char in enumerate(s):
            if pointer < len(spaces) and i == spaces[pointer]:
                res += ' '
                pointer += 1
            res += char
        return res
            
                