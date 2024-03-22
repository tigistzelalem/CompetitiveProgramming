class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        
        pre_sum = [0]*(len(s)+1)
        for left, right, dir_ in shifts:
            if dir_ == 1:
                pre_sum[left] +=  1 
                pre_sum[right + 1] -= 1
            else:
                pre_sum[left] -= 1
                pre_sum[right + 1] += 1

        for i in range(1, len(s)):
            pre_sum[i] += pre_sum[i-1]

        ans = []
        for i, char in enumerate(s):
            curr = (ord(char) - ord('a') + pre_sum[i]) % 26
            ans.append(chr(curr + ord('a')))
        

        return ''.join(ans)

                
