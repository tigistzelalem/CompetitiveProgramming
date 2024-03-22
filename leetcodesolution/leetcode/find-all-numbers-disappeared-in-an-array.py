class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        
        answer = []
        for i in range(1, n+1):
            if i not in counts:
                answer.append(i)
        
        return answer

