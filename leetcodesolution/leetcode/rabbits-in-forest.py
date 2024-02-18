class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = {}
        ans = 0
        for val in answers:
            count[val] = 1 + count.get(val, 0)
        
        for key, val in count.items():
            if val == 1:
                ans += key + 1
            else:
                ans += math.ceil(val/ (key + 1)) * (key + 1)

        return ans            