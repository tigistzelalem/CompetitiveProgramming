class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = Counter(students)
        
        for sand in sandwiches:
            if count[sand] > 0:
                count[sand] -= 1
            else:
                return count[not sand]
        return 0
