class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_ = max(candies)
        arr = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_:
                arr.append(True)
            else:
                arr.append(False)

        return arr