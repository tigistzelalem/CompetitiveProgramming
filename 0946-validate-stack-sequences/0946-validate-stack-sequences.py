class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i =0
        j =0
        while j < len(popped):
            if stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
            elif i < len(pushed):
                stack.append(pushed[i])
                i += 1
            else:
                return False
        return True
        