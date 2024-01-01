class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        counter = Counter(nums)
        sorted_nums = sorted(set(nums), reverse=True)
        count = 0
        ops = 0
        for i in sorted_nums[:-1]:
            count += counter[i]
            ops += count
        
        return ops
                