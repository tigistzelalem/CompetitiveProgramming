class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        pre_sum = [0]*1001
        total = 0
        for trip in trips:
            pre_sum[trip[1]] += trip[0]
            pre_sum[trip[2]] -= trip[0]
        
        for passenger in pre_sum:
            total += passenger
            if total > capacity:
                return False
        
        return True



                       
            
        