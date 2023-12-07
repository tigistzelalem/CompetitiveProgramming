class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less_than_pivot = []
        greater_than_pivot = []

        for num in nums:
            if num > pivot:
              greater_than_pivot.append(num)   
            elif num < pivot:
               less_than_pivot.append(num)
            else:
              greater_than_pivot.insert(0, num)
        
                  
        return less_than_pivot + greater_than_pivot
