class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack =[]
        reverse = ""
        for char in s:
            if char != ")":
                stack.append(char)
            else:
                reverse = ''
                while stack[-1] != "(":
                    reverse += stack.pop() 
                stack.pop()
                for val in reverse:
                    stack.append(val)
        return ''.join(stack)
          


