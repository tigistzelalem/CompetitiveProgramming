class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = []
        for i in range (len(position)):
            fleet.append([position[i], speed[i]])
        fleet.sort(reverse=True)
        stack = []
        for x,v in fleet:
            dist = target - x
            if not stack:
                stack.append(dist/v)
            elif dist/v > stack[-1]:
                stack.append(dist/v)
        return len(stack)
            
            
        
