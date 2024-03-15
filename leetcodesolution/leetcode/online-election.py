class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.leaders = []
        self.count = {}
        leader = None
        for person in persons:
            self.count[person] = 1 + self.count.get(person, 0)
            if leader is None or self.count[person] >= self.count.get(leader, 9):
                leader = person
            self.leaders.append(leader)


    def q(self, t: int) -> int:
        left = 0
        right = len(self.times) -1 
        while left <= right:
            mid = (left + right) // 2
            if self.times[mid] <= t:
                left = mid + 1
            else:
                right = mid - 1
    
        return self.leaders[left - 1]
    
    
        


        
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)