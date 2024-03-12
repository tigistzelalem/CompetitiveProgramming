class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        dict_ = {}
        for i, interval in enumerate(intervals):
            dict_[interval[0]] = i
        
        intervals.sort()
        n = len(intervals)

        def bs(interval, target):
            left = 0
            right = n - 1
            while left <= right:
                mid = (left + right) // 2
                if intervals[mid][0] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            if left == n:
                return -1
            else:
                return left
        
        ans = [-1]*n
        for i in range(n):
            idx = bs(intervals, intervals[i][1])
            if idx != -1:
                ans[dict_[intervals[i][0]]] = dict_[intervals[idx][0]]
            else:
                ans[dict_[intervals[i][0]]] = -1
        
        return ans



            
          