class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k > len(num):
            return "0"
        stack = []
        for i in range(len(num)):
            while k > 0 and stack and num[i] < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(num[i])
        while k > 0:
            stack.pop()
            k -= 1
        while stack and stack[0] == '0':
            stack.pop(0)
        return ''.join(stack) if stack else '0'
