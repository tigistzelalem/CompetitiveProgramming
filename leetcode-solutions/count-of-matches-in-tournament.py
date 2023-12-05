class Solution:
    def numberOfMatches(self, n: int) -> int:
        if n ==  1:
            return 0
        num = n
        count = 0
        for i in range(num):
            count += n // 2
            n = n - n//2
        
        return count
