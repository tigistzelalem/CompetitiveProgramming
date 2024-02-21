class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # left = 0
        # right = len(s) -1 
        # while left < right:
        #     s[left], s[right] = s[right], s[left]
        #     left += 1
        #     right -= 1
        def reverse(s, start, end):
            if start > end:
                return
            
            s[start], s[end] = s[end], s[start]
            reverse(s, start + 1, end - 1)

        reverse(s, 0, len(s) - 1)
    

                
        
       
            
            
            