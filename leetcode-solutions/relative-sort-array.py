class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        max_ = max(max(arr1), max(arr2))
        counts = [0]*(max_ + 1)

        for num in arr1:
            counts[num] += 1
        
        ans = []
        for num in arr2:
            while counts[num] > 0:
                ans.append(num)
                counts[num] -= 1
        for i in range(len(counts)):
            while counts[i] > 0:
                ans.append(i)
                counts[i] -= 1
        

        return ans

       
                
       



      



       
