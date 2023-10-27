class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        left = 0
        right = n 
        result = []
        
        for char in s:
            if char == "I":
                result.append(left)
                left += 1
            else:
                result.append(right)
                right -= 1
        
        return result + [left]
                
      

                    
       