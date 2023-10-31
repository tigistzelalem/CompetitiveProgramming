class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        left = 0
        right = 0
        count = 0
        
        while left < len(heights) and right < len(expected):
            if heights[left] == expected[right]:
                left += 1
                right += 1
            else:
                count += 1
                left += 1
                right += 1                                
        
        return count
            
