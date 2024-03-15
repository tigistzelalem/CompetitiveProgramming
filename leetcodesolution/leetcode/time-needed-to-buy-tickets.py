class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n=len(tickets)
        queue=deque([i for i in range(n)])
        
        time=0
        
        while queue:
            for i in range(len(queue)):

                val=queue.popleft()
                tickets[val]-=1

                if tickets[val]>=1:
                    queue.append(val)
                
                time+=1
                if tickets[k]==0:
                    return time