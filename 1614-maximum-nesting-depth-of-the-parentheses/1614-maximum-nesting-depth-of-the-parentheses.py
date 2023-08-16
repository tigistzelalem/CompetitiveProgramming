class Solution:
    def maxDepth(self, s: str) -> int:
        
        stack = []
        count = 0
        
        for char in s:
            if char == '(':
                stack.append(char)
                
                if len(stack) > count:
                    count = len(stack)
            elif char == ')':
                stack.pop()
        return count