class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                sub = ""
                while stack[-1] != "[":
                    sub = stack.pop() + sub
                stack.pop()

                res = ""
                while stack and stack[-1].isdigit():
                    res = stack.pop() + res
                stack.append(int(res)*sub)
            
        return ''.join(stack)
            
