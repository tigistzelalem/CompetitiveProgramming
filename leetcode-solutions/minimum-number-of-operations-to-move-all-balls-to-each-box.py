class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        arr = [0]*n

        for i in range(n):
            total_ops = 0
            for j in range(n):
                if i != j and boxes[j] == '1':
                    total_ops += abs(j-i)
            
            arr[i] = total_ops
        
        return arr


