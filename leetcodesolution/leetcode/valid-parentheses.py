class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        for ele in s:
            if ele == "(" or ele == "{" or ele == "[":
                stack.append(ele)
            else:
                if not stack:
                    return False
                elif ele == ")" and stack[-1] == "(":
                    stack.pop()
                elif ele == "}" and stack[-1] == "{":
                    stack.pop()
                elif ele == "]" and stack[-1] == "[":
                    stack.pop()
                else:
                    return False

        return not stack
        