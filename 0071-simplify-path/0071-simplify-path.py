class Solution:
    def simplifyPath(self, path: str) -> str:
        
        stack = []
        path = path.split('/')
        
        for ele in path:
            if stack and ele == '..':
                stack.pop()
            elif ele not in ('.', '', '..'):
                stack.append(ele)
        return '/' + '/'.join(stack)