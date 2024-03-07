class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
            left = 1
            right = max(piles)
            def canEat(mid):
                return sum(ceil(i/mid) for i in piles) <= h
            
            while left < right:
                mid = (left + right) // 2
                if canEat(mid):
                    right = mid
                else:
                    left = mid + 1
            
            return left