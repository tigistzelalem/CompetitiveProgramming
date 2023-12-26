class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        count = 0
        max_flips = 0

        for i in range(len(flips)):
            max_flips = max(max_flips, flips[i])
            if max_flips == i+1:
                count += 1
        return count


        