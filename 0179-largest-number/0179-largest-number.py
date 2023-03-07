class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        num_strings = [str(num) for num in nums]
        num_strings.sort(key=lambda x: x*10, reverse=True)
        return str(int(''.join(num_strings)))

