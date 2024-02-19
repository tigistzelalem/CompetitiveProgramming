class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        count = 0
        for ele in s:
            if ele == "(":
                stack.append(0)
            else:
                popped = stack.pop()
                val = max(1, 2*popped)

                stack[-1] += val
            
        return stack.pop()
