class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        
        if not nums:
            return result

        start = end = nums[0]

        for num in nums[1:]:
            if num == end + 1:
                end = num
            else:
                if start == end:
                    result.append(str(start))
                else:
                    result.append(str(start) + "->" + str(end))
                start = end = num

        if start == end:
            result.append(str(end))
        else:
            result.append(str(start) + "->" + str(end))

        return result
