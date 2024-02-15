class Solution:
    def numberOfWays(self, s: str) -> int:
        
        ans = 0
        zeros = 0
        ones = 0
        ones_op = zeros_op = 0

        for val in s:
            if val == "1":
                ans += ones_op
                zeros_op += zeros
                ones += 1
            else:
                ans += zeros_op
                ones_op += ones
                zeros += 1
        
        return ans
