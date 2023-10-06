class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        
        Sum = skill[0] + skill[-1]
        ans = 0
        for i in range(len(skill)//2):
            if skill[i] + skill[-i-1] == Sum:
                ans +=(skill[i]*skill[-i-1])
            else:
                return -1
        
        return ans
        