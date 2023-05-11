class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n < 0:
            return pow(1/x, -n)
        elif n % 2 == 0:
            y = pow(x, n//2)
            return y * y
        else:
            return x * pow(x, n-1)