class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
       
        ans = []
        
        def backtrack(left, right, s):
            if len(s) == n * 2 and s not in ans:
                ans.append(s)
                return

            if left < n:
                backtrack(left + 1, right,s + '(')

            if right < left:
                backtrack(left, right + 1,s + ')')

        backtrack(0, 0,'')
        return ans



