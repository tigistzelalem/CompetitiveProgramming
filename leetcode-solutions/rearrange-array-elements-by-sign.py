class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = []
        negative = []

        for num in nums:
            if num > 0:
                positive.append(num)
            else:
                negative.append(num)

        result = []
        max_len = max(len(positive), len(negative))
        for i in range(max_len):
            result.append(positive[i])
            result.append(negative[i])

        return result  