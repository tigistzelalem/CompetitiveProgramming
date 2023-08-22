class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)

        arr.sort(key=lambda num: abs(num - x))

        ans = sorted(arr[:k])
        return ans
