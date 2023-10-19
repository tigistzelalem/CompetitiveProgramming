class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        
        num_str = str(num)
        count = 0
        
        for i in range(len(num_str) - k + 1):
            substr = num_str[i:i+k]
            
            if substr[0] != 0:
                subnum = int(substr)
                
                if subnum != 0 and num % subnum == 0:
                    count += 1
                    
        return count
        

    