class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        opened = 0
        
        for i in s:
            if i == '(' and opened > 0:
                stack.append(i)
            elif i == ')' and opened > 1:
                stack.append(i)
            opened += 1 if i == '(' else -1
        return ''.join(stack)
            
