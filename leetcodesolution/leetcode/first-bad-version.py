# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        left = 1
        right = n
        mid = 0
        while left < right:
            mid = (left + right) // 2
            bad = isBadVersion(mid)

            if bad:
                right = mid
            else:
                left = mid + 1
            
        return right
            

