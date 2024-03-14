class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        def find_sum(divisor):
            sum_ = 0
            for num in nums:
                sum_ += ceil(num / divisor)
            return sum_
        

        left = 1
        right = max(nums)
        while left < right:
            mid = (left + right) // 2
            sum_ = find_sum(mid)
            if sum_ <= threshold:
                right = mid 
            else:
                left = mid + 1
        
        return right
            