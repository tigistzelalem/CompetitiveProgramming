class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mp = {"2":"abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        ans = []

        if not digits:
            return []
        
        def backtrack(comb, digit):
            if not digit:
                ans.append(comb)
                return
            
            for char in mp[digit[0]]:
                backtrack(comb + char, digit[1:])
                print(digit)

        backtrack("", digits)
        return ans
            

            