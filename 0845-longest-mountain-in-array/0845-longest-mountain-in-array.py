class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        count = 0
        ans = 0
        n = len(arr)
        
        for i in range(1, n-1):
            if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                count = 1
                p1 = i
                p2 = i
                
                while p1 > 0 and arr[p1] > arr[p1-1]:
                    count += 1
                    p1 -= 1
                while p2 < n-1 and arr[p2] > arr[p2+1]:
                    p2+=1
                    count += 1
            ans = max(ans, count)
            count = 0
        return ans
                    