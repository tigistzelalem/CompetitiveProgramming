class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points = sorted(point[0] for point in points)
        max_diff = 0
        for i in range(1, len(points)):
            width = points[i] - points[i-1]
            max_diff = max(max_diff, width)

        return max_diff
          
        