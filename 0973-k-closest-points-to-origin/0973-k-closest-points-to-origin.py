class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for point in points:
            distance = math.sqrt(point[0] ** 2 + point[1] ** 2)
            distances.append((distance, point))
        distances.sort()
        return [point[1] for point in distances[:k]]