class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        min_ = float("inf")

        for num in nums:
            while stack and stack[-1][0] <= num:
                stack.pop()
            
            if stack and stack[-1][1] < num:
                return True
            min_ = min(min_, num)
            stack.append([num, min_])
            
        
        return False
