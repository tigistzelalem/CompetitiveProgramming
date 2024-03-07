class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        totalWeight = 0
        maxWeight = -1
        for weight in weights:
            maxWeight = max(maxWeight, weight)
            totalWeight += weight
        
        left = maxWeight
        right = totalWeight
        while left < right:
            mid = (left + right) // 2
            neededDays = 1
            currWeight = 0
            for weight in weights:
                if currWeight + weight > mid:
                    neededDays += 1
                    currWeight = 0
                currWeight += weight
            if neededDays > days:
                 left = mid + 1
            else:
                right = mid
        
        return left