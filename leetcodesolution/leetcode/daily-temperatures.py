class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        for i, val in enumerate(temperatures):
            
            while stack and temperatures[stack[-1]] < val:
                diff = stack.pop()
                res[diff] = i - diff
            stack.append(i)

        return res 