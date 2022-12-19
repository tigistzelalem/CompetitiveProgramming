class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 and x ==1:
            return x
        min = 0
        max = x
        while min <= max:
            mid = (min+max) // 2
            sqr = mid**2
            if sqr == x:
                return mid
            elif sqr < x:
                min = mid +1
                ans = mid
            else:
                max = mid -1
        return ans
           











    
            
            
        