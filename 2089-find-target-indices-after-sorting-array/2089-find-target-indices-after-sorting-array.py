class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        values = sorted(nums)
        list1 = []
        for i in range(len(values)):
            val = values[i]
            if val == target:
                    list1.append(i)
        return list1
      
