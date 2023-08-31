class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        
        nums.sort()
        ans = []
        
        for i in queries:
            count = 0
            for num in nums:
                if i >= num:
                    i -= num
                    count += 1
                else:
                    break
            ans.append(count)
        return ans