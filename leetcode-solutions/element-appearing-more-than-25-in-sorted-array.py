class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        
        duplicate = len(arr) // 4
        counts = defaultdict(int)

        for i in range(len(arr)):
                counts[arr[i]] += 1
        for i in arr:
            if counts[i] > duplicate:
                return i

       