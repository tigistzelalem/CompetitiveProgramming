class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        pre_sum = [0]*(n)
        for first, last, seats in bookings:
            pre_sum[first - 1] += seats
            if last < n:
                pre_sum[last] -= seats
        
        for i in range(1,n):
            pre_sum[i] += pre_sum[i-1]
        
        return pre_sum            
            
       