class Solution:
    def pivotInteger(self, n: int) -> int:
        
        ans = []
        
        for i in range(1,n + 1):
            ans.append(i)
            
        for i in range(len(ans)):
                if sum(ans[:i]) == sum(ans[i+1:]):
                    return ans[i]
        return -1
                
            