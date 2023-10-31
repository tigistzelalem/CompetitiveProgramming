class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sum_ = (sum(aliceSizes) - sum(bobSizes)) /2
        sets = set(aliceSizes)
        
        for i in bobSizes:
            if sum_ + i in sets:
                return [sum_ + i, i]
        