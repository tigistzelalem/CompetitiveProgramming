class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        answer = []
        for i in range(len(l)):
            arth = sorted(nums[l[i]:r[i]+1])
            if len(arth) == 1 or len(arth) == 2:
                answer.append(True)
                continue
            is_arth = True
            for j in range(1,len(arth)-1):
                if arth[j] - arth[j-1] != arth[j+1] - arth[j]:
                    is_arth = False
            answer.append(is_arth)
        return answer
                
           
