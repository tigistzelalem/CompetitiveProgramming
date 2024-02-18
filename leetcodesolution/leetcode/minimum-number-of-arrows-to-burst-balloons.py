class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[1], x[0]))
        start = points[0][0]
        end = points[0][1]
        count = 1
        for i in range(1, len(points)):
            if points[i][0] <= end:
                start = max(start, points[i][0])
                end = min(end, points[i][1])
            else:
                start = points[i][0]
                end = points[i][1]
                count += 1

        return count
               
            
           
        