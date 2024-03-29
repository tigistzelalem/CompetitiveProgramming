class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        max_index = 0
        for i in range(len(arr)):
            if arr[i] >= arr[max_index]:
                max_index = i
            
        if max_index == 0 or max_index == len(arr) - 1:
            return False
        
        for i in range(max_index):
            if arr[i] >= arr[i+1]:
                return False
        
        for i in range(max_index, len(arr)-1):
            if arr[i] <= arr[i+1]:
                return False

        return True

                
