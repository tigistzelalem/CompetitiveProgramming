class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 1000000007
        odd =  pow(4, n // 2, mod)
        even = pow(5, (n+1) // 2 , mod)
       
        return even*odd % mod





       