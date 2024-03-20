from typing import List

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        arr = sorted(nums)
        result = []

        for num in nums:
            idx = bisect.bisect_left(arr, num)
            del arr[idx]

            if idx == -1:
                result.append(0)
            else:
                result.append(idx)
        
        return result
