class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # if n <= 0:
        #     return False
        # while n % 4 == 0:
        #     n /= 4
        
        # return n == 1
        if n == 0:
            return False
        elif n == 1:
            return True
        n /= 4
        return self.isPowerOfFour(n)

