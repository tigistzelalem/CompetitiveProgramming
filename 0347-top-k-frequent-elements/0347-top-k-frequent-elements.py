class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num = Counter(nums)
        val = list(num.values())
        val.sort(reverse=True)
        top = val[:k]
        res = []
        for key in num.keys():
                if num[key] in top:
                    res.append(key)
        return res