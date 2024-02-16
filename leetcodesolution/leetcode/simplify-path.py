class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split("/")

        for element in path:
            if stack and element == "..":
                stack.pop()
            elif element not in ('.', '', '..'):
                stack.append(element)
        
        return '/' + '/'.join(stack)

        