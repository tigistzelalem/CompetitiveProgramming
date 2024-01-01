class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        price = 0
        count = 0
        for i in range(len(costs)):
            if costs[i] > coins:
                return count
            if price + costs[i] <= coins:
                price += costs[i]
                count += 1

        return count

