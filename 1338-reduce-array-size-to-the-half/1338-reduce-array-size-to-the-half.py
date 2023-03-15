class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        val = Counter(arr)
        lis = list(val.values())
        lis.sort(reverse=True)
        initial = len(arr)
        target = len(arr)//2
        mini = 0
        for i in lis:
            if initial > target:
                initial -=i
                mini +=1
            else:
                break
        return mini
    