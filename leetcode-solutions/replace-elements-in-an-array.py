class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:

        positions = {}
        for i , num in enumerate(nums):
            positions[num] = i
        
        for operation in operations:
            old, new = operation
            if old in positions:
                pos = positions[old]
                nums[pos] = new
                positions[new] = pos
                del positions[old]

        return nums


            

            