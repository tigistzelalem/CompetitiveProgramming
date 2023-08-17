class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        
        max_arr = arr[0]
        count = 0
        
        for i in range(len(arr)):
            if max_arr < arr[i]:
                max_arr = arr[i]
            
            if max_arr == i:
                count += 1
        return count