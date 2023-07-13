class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in operations:
            if any(map(str.isdigit, i)):
                stack.append(int(i))
            if i == "+":
                stack.append(stack[-1] + stack[-2])
            elif i == "D":
                stack.append(2*stack[-1])
            elif i == "C":
                stack.pop()
        return sum(stack)

        